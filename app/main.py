from fastapi import FastAPI
from app.api.v1 import routes as v1_routes

app = FastAPI(title="API Example")
app.include_router(v1_routes.router, prefix="/v1")
