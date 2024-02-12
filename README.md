# OpenAI Pricing API

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



http://localhost:8000/api/v1/calculate_cost/

Request example
```
{"company": "openai", "endpoint": "/v1/chat/completions", "requestBody": "eyJtb2RlbCI6ImdwdC00IiwibWVzc2FnZXMiOlt7InJvbGUiOiJ1c2VyIiwiY29udGVudCI6ImdpdmUgbWUgYSBoYWlrdSBhYm91dCBwbGFuZXRzIn0seyJyb2xlIjoic3lzdGVtIiwiY29udGVudCI6IlNwaGVyZXMgb2YgbXlzdGlxdWUgZGFuY2UsXG5JbiBjb3NtaWMgYmFsbGV0IHRoZXkgd2hpcmwsXG5QbGFuZXRhcnkgdHJhbmNlLiJ9LHsicm9sZSI6InVzZXIiLCJjb250ZW50IjoiY2FuIHlvdSBpbmNsdWRlIHBsdXRvPyJ9XX0=", "responseBody": "eyJpZCI6ImNoYXRjbXBsLThwelo2VUt6ZmJJVVJPV3o3SXhUM0dsME53ZHhHIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uIiwiY3JlYXRlZCI6MTcwNzQwMjA3NiwibW9kZWwiOiJncHQtNC0wNjEzIiwiY2hvaWNlcyI6W3siaW5kZXgiOjAsIm1lc3NhZ2UiOnsicm9sZSI6ImFzc2lzdGFudCIsImNvbnRlbnQiOiJFdmVuIHNtYWxsIFBsdXRvLFxuRGFuY2VzIGluIGNlbGVzdGlhbCB3YWx0eixcbkluIHRoZSB2b2lkLCBzbyBtdXRlLiJ9LCJsb2dwcm9icyI6bnVsbCwiZmluaXNoX3JlYXNvbiI6InN0b3AifV0sInVzYWdlIjp7InByb21wdF90b2tlbnMiOjQ1LCJjb21wbGV0aW9uX3Rva2VucyI6MTksInRvdGFsX3Rva2VucyI6NjR9LCJzeXN0ZW1fZmluZ2VycHJpbnQiOm51bGx9"}
```

Response example
```
{"cost": 500}
```

Testing

To run the test suite, use:

```bash
make test
```

