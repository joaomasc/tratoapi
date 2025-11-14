from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database.connection import Base


class Trato(Base):
    """Modelo de Trato para gerenciamento de alimentação de animais"""
    __tablename__ = "tratos"
    
    id = Column(Integer, primary_key=True, index=True)
    animal_batch = Column(String, index=True, nullable=False)
    feed_type = Column(String, nullable=False)
    silo_weight_before = Column(Float, nullable=False)
    silo_weight_after = Column(Float, nullable=False)
    weight_supplied = Column(Float, nullable=False)
    feeding_datetime = Column(DateTime, default=datetime.now, nullable=False)
