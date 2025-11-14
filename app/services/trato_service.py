from sqlalchemy.orm import Session
from app.models.trato import Trato
from app.schemas.trato import TratoCreate, TratoUpdate
from typing import List, Optional
from datetime import datetime


class TratoService:
    
    @staticmethod
    def calculate_weight_supplied(weight_before: float, weight_after: float) -> float:
        return weight_before - weight_after
    
    @staticmethod
    def create_trato(db: Session, trato: TratoCreate) -> Trato:
        # Calcula o peso fornecido
        weight_supplied = TratoService.calculate_weight_supplied(
            trato.silo_weight_before, 
            trato.silo_weight_after
        )
        
        db_trato = Trato(
            animal_batch=trato.animal_batch,
            feed_type=trato.feed_type,
            silo_weight_before=trato.silo_weight_before,
            silo_weight_after=trato.silo_weight_after,
            weight_supplied=weight_supplied,
            feeding_datetime=datetime.now()
        )
        
        db.add(db_trato)
        db.commit()
        db.refresh(db_trato)
        return db_trato
    
    @staticmethod
    def get_trato(db: Session, trato_id: int) -> Optional[Trato]:
        return db.query(Trato).filter(Trato.id == trato_id).first()
    
    @staticmethod
    def get_tratos(db: Session, skip: int = 0, limit: int = 100) -> List[Trato]:
        return db.query(Trato).order_by(Trato.feeding_datetime.desc()).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_trato(db: Session, trato_id: int, trato_update: TratoUpdate) -> Optional[Trato]:
        db_trato = db.query(Trato).filter(Trato.id == trato_id).first()
        if not db_trato:
            return None
        
        # Atualiza apenas os campos fornecidos
        update_data = trato_update.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(db_trato, key, value)
        
        # Recalcula o peso fornecido com os novos valores
        db_trato.weight_supplied = TratoService.calculate_weight_supplied(
            db_trato.silo_weight_before,
            db_trato.silo_weight_after
        )
        
        db.commit()
        db.refresh(db_trato)
        return db_trato
    
    @staticmethod
    def delete_trato(db: Session, trato_id: int) -> bool:
        db_trato = db.query(Trato).filter(Trato.id == trato_id).first()
        if not db_trato:
            return False
        
        db.delete(db_trato)
        db.commit()
        return True
