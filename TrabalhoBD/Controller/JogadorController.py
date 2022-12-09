from fastapi import APIRouter
from pydantic import BaseModel

from Service.JogadorService import JogadorService

jogador = APIRouter()

service = JogadorService()


class Item(BaseModel):
    name: str


class ItemId(BaseModel):
    id: int


class ItemUpdate(BaseModel):
    id: int
    name: str


@jogador.post("/jogador")
async def root(item: Item):
    return service.create_jogador(item.name)


@jogador.post("/jogador/excluir")
async def excluir_jogador(item: ItemUpdate):
    return service.exclude_jogador(item.id)


@jogador.post("/jogador/atualizar")
async def excluir_jogador(item: ItemUpdate):
    return service.update_jogador(item.id, item.name)
