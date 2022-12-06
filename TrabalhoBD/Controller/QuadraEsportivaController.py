from fastapi import APIRouter
from pydantic import BaseModel

from Service.QuadraEsportivaService import QuadraEsportivaService

QuadraEsportiva = APIRouter()

service = QuadraEsportivaService()


class ItemCreate(BaseModel):
    tipo_de_quadra: str
    id_clube: int


class ItemId(BaseModel):
    id: int


@QuadraEsportiva.post("/quadra")
async def root(item: ItemCreate):
    return service.create_quadra(item.tipo_de_quadra, item.id_clube)


@QuadraEsportiva.post("/quadra/excluir")
async def excluir_quadra(item: ItemId):
    return service.exclude_quadra(item.id)
