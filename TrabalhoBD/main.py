from fastapi import FastAPI

from Controller.JogadorController import jogador
from Controller.ClubeController import clube
from Controller.TimeController import time

app = FastAPI()

app.include_router(jogador)
app.include_router(clube)
app.include_router(time)


@app.get("/")
async def root():
    return {"message": "Hello World"}
