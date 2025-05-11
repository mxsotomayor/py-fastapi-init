from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health.controller import router as health_routes
from app.routes.demo.controller import router as demo_routes

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(demo_routes, prefix="/v1")
app.include_router(health_routes, prefix="/v1")