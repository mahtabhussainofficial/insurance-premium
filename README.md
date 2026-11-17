# Insurance Premium Prediction API

> A FastAPI service that predicts an insurance premium category from customer and lifestyle information.

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-supported-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

## Overview

This service exposes a REST API for estimating an insurance premium category using a trained machine-learning model. It accepts a customer's age, body measurements, income, smoking status, city, and occupation, then derives features such as BMI, age group, lifestyle risk, and city tier before generating a prediction.

The API is suitable for local development, containerized deployment, and integration with web or mobile applications.

## Features

- FastAPI REST API with automatic OpenAPI documentation
- Input validation powered by Pydantic
- Automatic feature engineering for:
  - Body mass index (BMI)
  - Age group
  - Lifestyle risk
  - City tier
- Prediction confidence and class probabilities
- Health-check endpoint with model status and version
- Docker support

## Tech Stack

- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic
- pandas and NumPy
- scikit-learn
- Docker

## Project Structure

```text
.
├── app.py                    # FastAPI application and routes
├── config/
│   └── city_tier.py          # Tier 1 and Tier 2 city configuration
├── model/
│   ├── model.pkl             # Trained prediction model
│   └── predict.py            # Model loading and prediction logic
├── schemas/
│   ├── prediction_response.py # Prediction response schema
│   └── user_input.py          # Request validation and feature engineering
├── Dockerfile
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12 or later
- `pip`
- Docker (optional)

### Run Locally

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/mahtabhussainofficial/insurance-premium.git
   cd insurance-premium
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the API:

   ```bash
   uvicorn app:app --reload
   ```

The service is available at `http://localhost:8000`.

### Run with Docker

```bash
docker build -t insurance-premium-api .
docker run --rm -p 8000:8000 insurance-premium-api
```

## API Documentation

Once the service is running, interactive documentation is available at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- OpenAPI schema: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

## API Reference

### `GET /`

Returns a welcome message confirming that the API is available.

### `GET /health`

Returns the service status, model version, and whether the model loaded successfully.

Example:

```json
{
  "STATUS": "OK",
  "VERSION": "1.0.0",
  "MODEL_LOADED": true
}
```

### `POST /predict`

Predicts an insurance premium category from customer information.

Example request:

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "weight": 78,
    "height": 1.75,
    "income_lpa": 12,
    "smoker": false,
    "city": "Bengaluru",
    "occupation": "private_job"
  }'
```

The service derives BMI, age group, lifestyle risk, and city tier from the submitted values. A prediction contains the predicted category, confidence score, and probability for each supported category.

## Input Rules

| Field | Type | Requirements |
| --- | --- | --- |
| `age` | integer | Greater than 0 and less than 120 |
| `weight` | number | Greater than 0 |
| `height` | number | Greater than 0 and less than 2.5 meters |
| `income_lpa` | number | Greater than 0 |
| `smoker` | boolean | Whether the customer smokes |
| `city` | string | City name; normalized before tier classification |
| `occupation` | string | `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, or `private_job` |

## Derived Features

- **BMI:** `weight / height²`
- **Age group:** `young`, `adult`, `middle_aged`, or `senior`
- **Lifestyle risk:** `low`, `medium`, or `high`, based on smoking status and BMI
- **City tier:** Tier 1, Tier 2, or Tier 3 based on the configured city lists

## Development

Run the API with automatic reload during development:

```bash
uvicorn app:app --reload
```

Before deploying, verify the health endpoint and review the generated OpenAPI schema at `/docs`.

## License

No license has been specified for this repository. Add a license file before distributing or reusing the project.
