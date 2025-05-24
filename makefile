dev:
	.venv/Scripts/python.exe -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8002

dev-mac:
	.venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8000

migrate:
	.venv/Scripts/python.exe -m alembic revision --autogenerate -m "adding json mutable props"
	.venv/Scripts/python.exe -m alembic upgrade head