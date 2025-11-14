from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime


class TratoBase(BaseModel):
    """Schema base para Trato"""
    animal_batch: str = Field(
        ..., 
        min_length=1, 
        max_length=100, 
        description="Identificador do lote de animais"
    )
    feed_type: str = Field(
        ..., 
        min_length=1, 
        max_length=100, 
        description="Tipo de ração fornecida"
    )
    silo_weight_before: float = Field(
        ..., 
        gt=0, 
        description="Peso do silo antes de dispensar em quilogramas"
    )
    silo_weight_after: float = Field(
        ..., 
        ge=0, 
        description="Peso do silo depois de dispensar em quilogramas"
    )
    
    @field_validator('silo_weight_after')
    @classmethod
    def validate_weight_after(cls, v, info):
        """Valida que silo_weight_after não pode ser maior que silo_weight_before"""
        if 'silo_weight_before' in info.data and v > info.data['silo_weight_before']:
            raise ValueError('silo_weight_after não pode ser maior que silo_weight_before')
        return v


class TratoCreate(TratoBase):
    """Schema para criação de Trato"""
    pass


class TratoUpdate(TratoBase):
    """Schema para atualização de Trato"""
    animal_batch: Optional[str] = Field(None, min_length=1, max_length=100)
    feed_type: Optional[str] = Field(None, min_length=1, max_length=100)
    silo_weight_before: Optional[float] = Field(None, gt=0)
    silo_weight_after: Optional[float] = Field(None, ge=0)


class TratoResponse(BaseModel):
    """Schema de resposta para Trato"""
    id: int
    animal_batch: str
    feed_type: str
    silo_weight_before: float
    silo_weight_after: float
    weight_supplied: float = Field(description="Diferença calculada entre silo_weight_before e silo_weight_after")
    feeding_datetime: datetime = Field(description="Data e hora de registro do trato")
    
    class Config:
        from_attributes = True
