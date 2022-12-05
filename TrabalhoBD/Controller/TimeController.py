from fastapi import APIRouter
from pydantic import BaseModel

from Service.JogadorService import JogadorService
from Service.TimeService import TimeService

time = APIRouter()

service = TimeService()


class Item(BaseModel):
    name: str


class ItemId(BaseModel):
    id: int


@time.post("/time")
async def root(item: Item):
    return service.create_jogador(item.name)


@time.post("/time/excluir")
async def excluir_jogador(item: ItemId):
    return service.exclude_jogador(item.id)
