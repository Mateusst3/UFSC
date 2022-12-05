from fastapi import FastAPI

from Controller.JogadorController import jogador

app = FastAPI()

app.include_router(jogador)


@app.get("/")
async def root():
    return {"message": "Hello World"}
