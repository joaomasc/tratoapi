from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.trato import TratoCreate, TratoUpdate, TratoResponse
from app.services.trato_service import TratoService

router = APIRouter(
    prefix="/tratos",
    tags=["Tratos"]
)


@router.post("/", response_model=TratoResponse, status_code=status.HTTP_201_CREATED)
def create_trato(trato: TratoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo registro de trato.
    
    - **animal_batch**: Identificador do lote (ex: "Lote 05A", "Curral 12")
    - **feed_type**: Tipo de ração (ex: "Engorda", "Crescimento Inicial")
    - **silo_weight_before**: Peso do silo antes de dispensar (kg)
    - **silo_weight_after**: Peso do silo depois de dispensar (kg)
    
    O sistema calcula automaticamente:
    - **weight_supplied**: silo_weight_before - silo_weight_after
    - **feeding_datetime**: data/hora atual do registro
    """
    return TratoService.create_trato(db, trato)


@router.get("/", response_model=List[TratoResponse])
def list_tratos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Lista todos os registros de tratos existentes.
    
    - **skip**: Número de registros a pular (paginação)
    - **limit**: Número máximo de registros a retornar
    """
    return TratoService.get_tratos(db, skip=skip, limit=limit)


@router.get("/{trato_id}", response_model=TratoResponse)
def get_trato(trato_id: int, db: Session = Depends(get_db)):
    """
    Busca um único registro de trato pelo seu ID.
    
    Retorna HTTP 404 se o trato não for encontrado.
    """
    trato = TratoService.get_trato(db, trato_id)
    if not trato:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trato com ID {trato_id} não encontrado"
        )
    return trato


@router.put("/{trato_id}", response_model=TratoResponse)
def update_trato(trato_id: int, trato: TratoUpdate, db: Session = Depends(get_db)):
    """
    Atualiza um registro de trato existente.
    
    O weight_supplied é recalculado automaticamente com base nos novos valores.
    
    Retorna HTTP 404 se o trato não for encontrado.
    """
    updated_trato = TratoService.update_trato(db, trato_id, trato)
    if not updated_trato:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trato com ID {trato_id} não encontrado"
        )
    return updated_trato


@router.delete("/{trato_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trato(trato_id: int, db: Session = Depends(get_db)):
    """
    Remove um registro de trato do banco de dados.
    
    Retorna HTTP 204 No Content se bem-sucedido.
    Retorna HTTP 404 se o trato não for encontrado.
    """
    success = TratoService.delete_trato(db, trato_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trato com ID {trato_id} não encontrado"
        )
    return None
