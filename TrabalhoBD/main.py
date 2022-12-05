from fastapi import FastAPI
from Service.JogadorService import JogadorService

app = FastAPI()


service = JogadorService()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/jogador")
async def root(self):
    self.service.create_jogador('teste')
    return 'teste'