# differential-privacy-api
REST API for PII masking and differential privacy using FastAPI, Presidio &amp; Laplace mechanism


> REST API for PII masking and differential privacy using FastAPI, Presidio & Laplace mechanism
 
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
 
---
 
## Overview
 
**anonify** is a privacy-first microservice that acts as a data filter before storage or ML pipelines.
 
> 🚧 **Work in progress.** The project is under active development.
 
---
 
## Planned Endpoints
 
| Endpoint | Description |
|---|---|
| `POST /v1/pii/mask` | Detect and replace PII in unstructured text |
| `POST /v1/dp/noise` | Add Laplace noise to numerical data |
 
---
 
## Tech Stack
 
- **FastAPI** — REST API framework
- **Microsoft Presidio + spaCy** — PII detection
- **NumPy** — Laplace mechanism implementation
- **pytest** — Unit & integration testing
- **Docker + GitHub Actions + Kubernetes** — Containerization & CI/CD
---
 
## License
 
MIT © [kostas156](https://github.com/kostas156)