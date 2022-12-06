from fastapi import APIRouter
from pydantic import BaseModel

from Service.JogadorService import JogadorService
from Service.JogadorTimeService import JogadorTimeService
from Service.TimeQuadraService import TimeQuadraService
from Service.TimeService import TimeService

time = APIRouter()

service = TimeService()
service_jogador = JogadorTimeService()
service_quadra = TimeQuadraService()


class Item(BaseModel):
    name: str


class ItemId(BaseModel):
    id: int


class ItemIdJogadorTime(BaseModel):
    id_jogador: int
    id_time: int


class ItemIdTimeQuadra(BaseModel):
    horario: str
    id_time: int
    id_quadra: int


@time.post("/time")
async def root(item: Item):
    return service.create_jogador(item.name)


@time.post("/time/excluir")
async def excluir_jogador(item: ItemId):
    return service.exclude_jogador(item.id)


@time.post("/time/adicionarJogador")
async def adicionar_ao_time(item: ItemIdJogadorTime):
    return service_jogador.adicionar_ao_time(item.id_jogador, item.id_time)


@time.post("/time/reservarHorario")
async def reservar_horario(item: ItemIdTimeQuadra):
    return service_quadra.reservar_horario(horario=item.horario, id_quadra=item.id_quadra, id_time=item.id_time)
