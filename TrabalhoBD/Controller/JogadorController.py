from fastapi import APIRouter
from requests import post

from Service.JogadorService import JogadorService

jogador = APIRouter()

service = JogadorService()


@jogador.post("/jogador")
async def root():
    service.create_jogador('teste')
    return 'teste'
