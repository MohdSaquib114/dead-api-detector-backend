from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.api import API
from app.schema.api import APICreate, APIResponse
from app.services.health import calculate_health
from app.models.api_log import APILog
from fastapi import HTTPException

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/apis")
def create_api(api: APICreate, db: Session = Depends(get_db)):
    if not api.url.startswith("http"):
        raise HTTPException(status_code=400, detail="Invalid URL")

    new_api = API(**api.dict())
    db.add(new_api)
    db.commit()
    db.refresh(new_api)
    return new_api

@router.get("/apis", response_model=list[APIResponse])
def get_apis(db: Session = Depends(get_db)):
    return db.query(API).all()

@router.get("/apis/{api_id}/health")
def get_api_health(api_id: int, db: Session = Depends(get_db)):
    return calculate_health(api_id, db)

@router.get("/apis/{api_id}/logs")
def get_api_logs(api_id: int, db: Session = Depends(get_db)):
    logs = (
        db.query(APILog)
        .filter(APILog.api_id == api_id)
        .order_by(APILog.checked_at.desc())
        .limit(100)
        .all()
    )

    return logs

@router.delete("/apis/{api_id}")
def delete_api(api_id: int, db: Session = Depends(get_db)):
    api = db.query(API).filter(API.id == api_id).first()

    if not api:
        raise HTTPException(status_code=404, detail="API not found")

    db.delete(api)
    db.commit()

    return {"message": "API deleted successfully"}