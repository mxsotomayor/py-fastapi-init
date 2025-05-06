dev:
	.venv/Scripts/python.exe -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8000

dev-mac:
	.venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8000

migrate:
	.venv/Scripts/python.exe -m alembic revision --autogenerate -m "adding role text to staff"
	.venv/Scripts/python.exe -m alembic upgrade head