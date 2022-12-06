from fastapi import FastAPI

from Controller.ContratanteController import contratante
from Controller.JogadorController import jogador
from Controller.ClubeController import clube
from Controller.QuadraEsportivaController import QuadraEsportiva
from Controller.TimeController import time

app = FastAPI()

app.include_router(jogador)
app.include_router(clube)
app.include_router(time)
app.include_router(QuadraEsportiva)
app.include_router(contratante)


@app.get("/")
async def root():
    return {"message": "Hello World"}
