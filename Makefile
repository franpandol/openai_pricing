# Makefile

# Variables
SUPERUSER_NAME ?= admin
SUPERUSER_EMAIL ?= admin@example.com
SUPERUSER_PASSWORD ?= admin

# Run the app
run:
	docker-compose up

# Seed the database with pricing data
seed_pricing:
	docker-compose run web python manage.py seed_pricings

# Create a superuser account
createsuperuser:
	docker-compose run -e DJANGO_SUPERUSER_USERNAME=$(SUPERUSER_NAME) -e DJANGO_SUPERUSER_EMAIL=$(SUPERUSER_EMAIL) -e DJANGO_SUPERUSER_PASSWORD=$(SUPERUSER_PASSWORD) web python manage.py createsuperuser --noinput

# Shortcut to run all setup commands
setup: seed_pricing createsuperuser

.PHONY: run seed_pricing createsuperuser setup
