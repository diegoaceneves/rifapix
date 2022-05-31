# rifapix

Rifa Pix API

## Running

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn rifapix.api:api
```

## TO-DO

* API:
  * correct status when try add a unique item twice or delete an nonexistent iten.

* Validation
  * Password
  * Pix Integration
