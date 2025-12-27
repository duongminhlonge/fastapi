from fastapi import FastAPI
from app.api.v1 import routes as v1_routes
import uvicorn


app = FastAPI(title="API Example")
app.include_router(v1_routes.router, prefix="/v1")

# Add this to use debug (before run debug please don't run uvicorn app.main:app --reload)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
