import json
from django.test import TestCase



class PriceModelTestCase(TestCase):

    def setUp(self):
        from pricing.models import Price

        self.sample_price = Price.objects.create(
            base_price=10.00,
            prompt_price=5.00,
            completion_price=7.00,
            model="Test Model",
            company="Test Company",
            endpoint="Test Endpoint",
            calculation_type="tokens",
            size="Test Size",
            quality="Test Quality"
        )
    
    def test_calculate_cost_using_tokens(self):
        response_body = {"usage": {"prompt_tokens": 1000, "completion_tokens": 2000}}
        expected_cost = 19  # Calculation: (1000 * 5 / 1000) + (2000 * 7 / 1000) = 5 + 14 = 19
        self.assertEqual(self.sample_price.calculate_cost_using_tokens(response_body), expected_cost)

    def test_calculate_price_tokens(self):
        request_body = {"n": 10}
        response_body = {"usage": {"prompt_tokens": 1000, "completion_tokens": 2000}}
        expected_cost = 19  # Calculation: (1000 * 5 / 1000) + (2000 * 7 / 1000) = 5 + 14 = 19
        self.assertEqual(self.sample_price.calculate_price(request_body, response_body), expected_cost)

    def test_calculate_cost_using_images(self):
        request_body = {"n": 5}
        expected_cost = 50.00  # Calculation: 5 * 10 = 50
        self.assertEqual(self.sample_price.calculate_cost_using_images(request_body), expected_cost)

    def test_calculate_price_images(self):
        self.sample_price.calculation_type = "images"
        request_body = {"n": 5}
        expected_cost = 50.00  # Calculation: 5 * 10 = 50
        self.assertEqual(self.sample_price.calculate_price(request_body, None), expected_cost)

    def test_invalid_calculation_type(self):
        self.sample_price.calculation_type = "invalid"
        with self.assertRaises(ValueError):
            self.sample_price.calculate_price(None, None)
