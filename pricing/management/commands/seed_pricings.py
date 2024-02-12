# management/commands/seed_pricings.py

from django.core.management.base import BaseCommand
from pricing.models import Price
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Seeds the database with example pricings'

    def handle(self, *args, **kwargs):
        pricings = [
            {
                "base_price": 0.01,
                "prompt_price": 0.02,
                "completion_price": 0.03,
                "model": "gpt-4",
                "company": "openai",
                "endpoint": "/v1/chat/completions",
                "calculation_type": "tokens",
            },
            {
                "base_price": 0.02,
                "prompt_price": 0.03,
                "completion_price": 0.04,
                "model": "dall-e-2",
                "company": "openai",
                "endpoint": "/v1/images/generations",
                "calculation_type": "images",
                "size": "large",
                "quality": "ultra-high"
            }
        ]
        print(Price.objects.all())
        for pricing in pricings:
            try:
                Price.objects.create(**pricing)
                self.stdout.write(self.style.SUCCESS(f"Successfully added pricing for {pricing['model']}"))
            except IntegrityError:
                self.stdout.write(self.style.WARNING(f"Pricing for {pricing['model']} already exists"))
