from fastapi import APIRouter
from pydantic import BaseModel

from Service.ClubeService import ClubeService

clube = APIRouter()

service = ClubeService()


class Item(BaseModel):
    name: str
    endereco: str


class ItemId(BaseModel):
    id: int


@clube.post("/clube")
async def root(item: Item):
    return service.create_clube(item.name, item.endereco)


@clube.post("/clube/excluir")
async def excluir_jogador(item: ItemId):
    return service.exclude_clube(item.id)
