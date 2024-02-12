import base64
from django.http import JsonResponse
from .models import Price
import json
    
from rest_framework.response import Response
from rest_framework.views import APIView


class CostAPIView(APIView):

    def find_options(self, request_body: str) -> str:
        """Finds the model used in the request body."""
        # Find the model in the request body
        model = request_body["model"]
        size = request_body.get("size", "")
        quality = request_body.get("quality", "")
        return model, size, quality

    def post(self, request):
        # Verify the request and return 400 if the values are not there
        if not all(key in request.data for key in ["endpoint", "company", "requestBody", "responseBody"]):
            return JsonResponse({"error": "Missing required fields"}, status=400)
        # Get the model and tokens from the request
        endpoint = request.data.get("endpoint", "")
        company = request.data.get("company", "").lower()

        # these two are base64 encoded, decode them
        openai_request_body = request.data.get("requestBody", "")
        openai_response_body = request.data.get("responseBody", "")
        # decode the base64 to obtain the rest of the data
        openai_request_body_decoded = base64.b64decode(openai_request_body).decode("utf-8")
        openai_response_body_decoded = base64.b64decode(openai_response_body).decode("utf-8")
        # validate the json
        try:
            openai_request_body_decoded = json.loads(openai_request_body_decoded)
            openai_response_body_decoded = json.loads(openai_response_body_decoded)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        # find the model from the openai_request_body
        model, size, quality = self.find_options(openai_request_body_decoded)
        # find the price record in the database
        price = Price.objects.get(model=model, company=company, size=size, quality=quality, endpoint=endpoint)
        price = price.calculate_price(request_body=openai_request_body_decoded, response_body=openai_response_body_decoded)

        # Return the cost in SMC, there are 10000 SMC in 1 USD
        return Response({"cost": price * 10000})


