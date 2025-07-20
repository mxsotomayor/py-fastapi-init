devw:
	.venv/Scripts/python.exe -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8002

migratew:
	.venv/Scripts/python.exe -m alembic revision --autogenerate -m "adding my key token"
	.venv/Scripts/python.exe -m alembic upgrade head

dev:
	docker compose up db -d && .venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8000

migrate:
	.venv/bin/python -m alembic revision --autogenerate -m "fixing database schema"
	.venv/bin/python -m alembic upgrade head