from fastapi import APIRouter
from pydantic import BaseModel

from Service.ContratanteQuadraService import ContratanteQuadraService
from Service.ContratanteService import ContratanteService

contratante = APIRouter()

service = ContratanteService()
quadra_service = ContratanteQuadraService()


class ItemCreate(BaseModel):
    nome: str
    telefone: str
    endereco: str


class ItemId(BaseModel):
    id: int


class ItemIdContratanteQuadra(BaseModel):
    horario: str
    id_contratante: int
    id_quadra: int


@contratante.post("/contratante")
async def root(item: ItemCreate):
    return service.create_contratante(item.nome, item.endereco, item.telefone)


@contratante.post("/contratante/excluir")
async def excluir_contratante(item: ItemId):
    return service.exclude_contratante(item.id)


@contratante.post("/contratante/contratanteQuadra")
async def adicionar_quadra(item: ItemIdContratanteQuadra):
    return quadra_service.reservar_horario(item.id_contratante, item.id_quadra, item.horario)
