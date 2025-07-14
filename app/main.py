from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health.controller import router as health_routes
from app.routes.devices.controller import router as devices_routes
from app.routes.feedback.controller import router as feedback_routes
from app.routes.callbacks.controller import router as callbacks_routes
from app.routes.my_key.controller import router as my_key_routes

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI(
    title="Basic API"
)
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
# 
app.include_router(health_routes, prefix="/v1")