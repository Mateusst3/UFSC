from fastapi import APIRouter
from pydantic import BaseModel

from Service.ContratanteService import ContratanteService

contratante = APIRouter()

service = ContratanteService()


class ItemCreate(BaseModel):
    nome: str
    telefone: str
    endereco: str

class ItemId(BaseModel):
    id: int


@contratante.post("/contratante")
async def root(item: ItemCreate):
    return service.create_contratante(item.nome, item.endereco, item.telefone)


@contratante.post("/contratante/excluir")
async def excluir_contratante(item: ItemId):
    return service.exclude_contratante(item.id)

