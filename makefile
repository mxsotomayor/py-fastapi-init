devw:
	.venv/Scripts/python.exe -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8002

migratew:
	.venv/Scripts/python.exe -m alembic revision --autogenerate -m "adding my key token"
	.venv/Scripts/python.exe -m alembic upgrade head

dev:
	.venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --reload --port 8000

migrate:
	.venv/bin/python -m alembic revision --autogenerate -m "adding roles"
	.venv/bin/python -m alembic upgrade head

build:
	docker build --no-cache -t clobe-bff-api .
	docker run -p 8000:8000 clobe-bff-api 
