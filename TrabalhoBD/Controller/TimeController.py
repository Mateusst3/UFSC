from fastapi import APIRouter
from pydantic import BaseModel

from Service.JogadorService import JogadorService
from Service.JogadorTimeService import JogadorTimeService
from Service.TimeService import TimeService

time = APIRouter()

service = TimeService()
service_jogador = JogadorTimeService()


class Item(BaseModel):
    name: str


class ItemId(BaseModel):
    id: int


class ItemIdJogadorTime(BaseModel):
    id_jogador: int
    id_time: int


@time.post("/time")
async def root(item: Item):
    return service.create_jogador(item.name)


@time.post("/time/excluir")
async def excluir_jogador(item: ItemId):
    return service.exclude_jogador(item.id)


@time.post("/time/adicionarJogador")
async def adicionar_ao_time(item: ItemIdJogadorTime):
    return service_jogador.adicionar_ao_time(item.id_jogador, item.id_time)
