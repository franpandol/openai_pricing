import json
from django.db import models


class Price(models.Model):
    COST_CALCULATION_CHOICES = [
        ("tokens", "Tokens"),
        ("images", "Images"),
    ]
    base_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    prompt_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    completion_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    model = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=100)
    calculation_type = models.CharField(
        max_length=100, choices=COST_CALCULATION_CHOICES
    )

    size = models.CharField(max_length=100, default="")
    quality = models.CharField(max_length=100, default="")

    class Meta:
        unique_together = ["model", "company"]

    def __str__(self):
        return f"{self.company} - {self.endpoint} - {self.model}"

    def calculate_cost_using_tokens(self, response_body):
        # get usage from response_body
        usage = response_body.get("usage")
        prompt_cost = usage.get("prompt_tokens") * self.prompt_price / 1000
        completion_cost = usage.get("completion_tokens") * self.completion_price / 1000
        total_cost = prompt_cost + completion_cost
        # round to 6 decimals
        total_cost = round(total_cost, 6)

        print(f"Total cost ${total_cost:.4f}\n")

        return total_cost

    def calculate_price(self, request_body, response_body):
        if self.calculation_type == "tokens":
            return self.calculate_cost_using_tokens(response_body)
        elif self.calculation_type == "images":
            return self.calculate_cost_using_images(request_body)
        else:
            raise ValueError("Invalid calculation type")

    def calculate_cost_using_images(self, request_body):
        # get the number of images from the request body
        num_images = request_body["n"]
        total_cost = num_images * self.base_price
        # round to 6 decimals
        total_cost = round(total_cost, 6)

        return total_cost
