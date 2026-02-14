# Demo REST Service

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Endpoints
- GET `/health`
- POST `/users` `{ "name": "...", "email": "..." }`
- GET `/users`
- GET `/users/{id}`
