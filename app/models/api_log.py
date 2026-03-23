from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey, DateTime
from datetime import datetime
from app.db.base import Base
from sqlalchemy.orm import relationship

class APILog(Base):
    __tablename__ = "api_logs"

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(Integer, ForeignKey("apis.id"))
    status_code = Column(Integer)
    response_time = Column(Float)
    is_success = Column(Boolean)
    checked_at = Column(DateTime, default=datetime.utcnow)

    api = relationship("API", back_populates="logs")