from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.db.session import SessionLocal
from app.models.api import API
from app.models.api_log import APILog
from app.services.checker import check_api

scheduler = AsyncIOScheduler()

async def monitor_apis():
    db = SessionLocal()
    apis = db.query(API).all()

    for api in apis:
        result = await check_api(api.url)

        log = APILog(
            api_id=api.id,
            status_code=result["status_code"],
            response_time=result["response_time"],
            is_success=result["is_success"]
        )

        db.add(log)

    db.commit()
    db.close()

def start_scheduler():
    scheduler.add_job(monitor_apis, "interval", seconds=30)
    scheduler.start()