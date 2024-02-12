# My Django Project

This Django project provides a RESTful API to calculate costs based on the usage of OpenAI's GPT and image generation models.

## Getting Started

### Prerequisites

To run this project, you'll need:

- Docker
- docker-compose

### Installation

1. Clone the repository:

```bash
git clone https://github.com/franpandol/openai_pricing.git
cd openai_pricing
```


Initial Setup

Before you can start using the API, you'll need to set up the database and create a superuser. You can do this easily using the make command.

Run the following command to seed the database with pricing examples and create a superuser:

```bash

make setup
```

The superuser credentials are only for local development
username: admin
password: admin

Using the API

Once the initial setup is complete, you can start the Django server using:

```bash
make run
```
The API provides endpoints to calculate costs for token-based or image-based requests. Detailed API documentation will be provided once the server is running, accessible at http://localhost:8000.
Testing

To run the test suite, use:

```bash
make test
```

