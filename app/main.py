from fastapi import FastAPI
from app.routes.api_routes import router
from app.workers.scheduler import start_scheduler

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    start_scheduler()