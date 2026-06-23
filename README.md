# 🔒 Anonify

> REST API for PII masking and differential privacy using FastAPI, Presidio & Laplace mechanism

[![CI](https://github.com/kostas156/differential-privacy-api/actions/workflows/ci.yml/badge.svg)](https://github.com/kostas156/differential-privacy-api/actions)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

**anonify** is a privacy-first microservice that acts as a data filter before storage or ML pipelines. It exposes two endpoints:

| Endpoint | Input | What it does |
|---|---|---|
| `POST /v1/pii/mask` | Free text | Detects and replaces PII with placeholder tokens |
| `POST /v1/dp/noise` | Numerical data | Adds calibrated Laplace noise to prevent reverse-engineering |

---

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI + Uvicorn |
| PII Detection | Microsoft Presidio + spaCy (`en_core_web_lg`) |
| Differential Privacy | Custom Laplace mechanism (NumPy) |
| Validation | Pydantic v2 |
| Testing | pytest (17 tests) |
| Containerization | Docker |
| CI | GitHub Actions |
| Orchestration | Kubernetes (manifests included) |

---

## Project Structure
```
Αnonify/
├── app/
│   ├── main.py               # FastAPI entry point
│   ├── config.py             # Settings via pydantic-settings
│   ├── api/v1/               # HTTP routing layer
│   │   ├── pii.py            # POST /v1/pii/mask
│   │   └── dp.py             # POST /v1/dp/noise
│   ├── core/
│   │   ├── pii/              # Presidio engine wrapper
│   │   └── privacy/          # Laplace mechanism
│   └── models/               # Pydantic request/response schemas
├── tests/
│   ├── unit/                 # Algorithm correctness tests
│   └── integration/          # Endpoint tests
├── k8s/                      # Kubernetes manifests
├── .github/workflows/        # CI pipeline
└── Dockerfile
```
---

## Quickstart

### Prerequisites

- Python 3.12+
- Docker (optional)

### Run Locally

```bash
git clone https://github.com/kostas156/differential-privacy-api.git
cd differential-privacy-api

pip install -r requirements.txt
python -m spacy download en_core_web_lg

uvicorn app.main:app --reload
```

API: `http://localhost:8000`
Swagger UI: `http://localhost:8000/docs`

### Run with Docker

```bash
docker build -t anonify .
docker run -p 8000:8000 anonify
```

---

## API Reference

### `POST /v1/pii/mask`

**Request:**
```json
{
  "text": "Hi, I'm John Doe. Reach me at john@example.com.",
  "entities": ["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER"]
}
```

**Response:**
```json
{
  "masked_text": "Hi, I'm [PERSON]. Reach me at [EMAIL_ADDRESS].",
  "detections": [
    { "entity_type": "PERSON", "start": 8, "end": 16, "score": 0.85 },
    { "entity_type": "EMAIL_ADDRESS", "start": 30, "end": 46, "score": 1.0 }
  ],
  "detection_count": 2
}
```

---

### `POST /v1/dp/noise`

**Request:**
```json
{
  "values": [120.5, 98.3, 150.0],
  "sensitivity": 1.0,
  "epsilon": 0.5
}
```

**Response:**
```json
{
  "noisy_values": [121.83, 96.14, 148.72],
  "epsilon": 0.5,
  "sensitivity": 1.0,
  "scale": 2.0
}
```

> **ε (epsilon):** Lower = stronger privacy, more noise. Range: `0.1` (strong) to `10.0` (weak).

---

## Differential Privacy: The Math

The Laplace mechanism adds noise drawn from:
noise ~ Laplace(0, Δf / ε)

- **Δf** (`sensitivity`) — max change a single record can cause in the query result
- **ε** (`epsilon`) — privacy budget; controls noise magnitude
- **scale** = `Δf / ε` — the Laplace distribution parameter

---

## Running Tests

```bash
pip install -r requirements-dev.txt
pytest tests/ -v
```

17 tests — 6 unit (Laplace), 5 unit (PII masker), 6 integration (endpoints).

---

## Deployment (Kubernetes)

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

## License

MIT © [Kostas](https://github.com/kostas156)