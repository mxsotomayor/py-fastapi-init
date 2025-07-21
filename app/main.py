import time
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from fastapi.responses import JSONResponse

from app.routes.health.controller import router as health_routes
from app.routes.devices.controller import router as devices_routes
from app.routes.feedback.controller import router as feedback_routes
from app.routes.callbacks.controller import router as callbacks_routes
from app.routes.my_key.controller import router as my_key_routes
from app.routes.users.controller import router as users_routes
from app.settings import Settings

setting = Settings()

API_KEY = setting.API_KEY
if not API_KEY:
    raise ValueError("API_KEY environment variable not set. Please set it in your .env file or environment.")


class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow OPTIONS requests to pass through (preflight requests for CORS)
        if request.method == "OPTIONS":
            response = await call_next(request)
            return response

        client_host = request.client.host

        if client_host in ["127.0.0.1", "::1", "localhost"]:
            print(f"Bypassing API key validation for localhost client: {client_host}")
            start_time = time.perf_counter()
            response = await call_next(request)
            process_time = time.perf_counter() - start_time
            response.headers["X-Process-Time"] = str(process_time)
            return response

        # Get the X-API-Key header from the request
        x_api_key = request.headers.get("X-API-Key")

        # Verify the API key
        if x_api_key is None or x_api_key != API_KEY:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid or missing X-API-Key header"},
                headers={"WWW-Authenticate": "Bearer"}, # Or "X-API-Key" if you prefer
            )

        # If API key is valid, proceed to the next middleware or route handler
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = str(process_time)

        return response

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI(
    title="Basic API"
)

app.add_middleware(APIKeyMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(devices_routes, prefix="/v1")
app.include_router(callbacks_routes, prefix="/v1")
app.include_router(feedback_routes, prefix="/v1")
app.include_router(my_key_routes, prefix="/v1")
app.include_router(users_routes, prefix="/v1")
# 
app.include_router(health_routes, prefix="/v1")