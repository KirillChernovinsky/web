from fastapi import APIRouter, Depends
from sqlalchemy import select, insert,update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation


from datetime import datetime
from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str


router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)



##########################################
@router.get("/get_type")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.fetchall()
###############################################


@router.get("/get_all")
async def get_all_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(operation)
    result = await session.execute(query)
    return result.fetchall()
##################################################################################




#Создание товара
@router.post("/operation_create")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}



#Обновление товара
@router.put("/operation_update")
async def update_specific_operation(operation_id: int, updated_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    query = update(operation).where(operation.c.id == operation_id).values(**updated_operation.dict(exclude_unset=True))
    result = await session.execute(query)
    await session.commit()
    return {"status": "upgrade_done"}




#Удаление
@router.delete("/operation_delete/{id}")
async def delete_specific_operation(operation_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(operation).where(operation.c.id == operation_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}