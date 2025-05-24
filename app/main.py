from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health.controller import router as health_routes
from app.routes.request.controller import router as requests_routes

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI(
    title="Gentoo Core"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(requests_routes, prefix="/v1")
app.include_router(health_routes, prefix="/v1")