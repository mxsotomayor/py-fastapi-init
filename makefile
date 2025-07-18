devw:
	.venv/Scripts/python.exe -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8002

dev:
	docker compose up db -d && .venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8000

migrate:
	.venv/bin/python -m alembic revision --autogenerate -m "adding my key token"
	.venv/bin/python -m alembic upgrade head