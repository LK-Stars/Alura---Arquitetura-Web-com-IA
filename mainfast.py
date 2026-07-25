from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de álbum de figurinhas", version="0.1.0")


class Figurinha(BaseModel):
    id: int
    nome: str
    numero: int
    repetida: bool = False


class FigurinhaCreate(BaseModel):
    nome: str
    numero: int
    repetida: bool = False


figurinhas_db: Dict[int, Figurinha] = {
    1: Figurinha(id=1, nome="Pelé", numero=10, repetida=False),
    2: Figurinha(id=2, nome="Messi", numero=30, repetida=True),
}


@app.get("/")
def home() -> dict:
    return {"message": "API de álbum de figurinhas está no ar!"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/figurinhas", response_model=list[Figurinha])
def listar_figurinhas() -> list[Figurinha]:
    return list(figurinhas_db.values())


@app.get("/figurinhas/{figurinha_id}", response_model=Figurinha)
def buscar_figurinha(figurinha_id: int) -> Figurinha:
    figurinha = figurinhas_db.get(figurinha_id)
    if figurinha is None:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada")
    return figurinha


@app.post("/figurinhas", response_model=Figurinha, status_code=201)
def criar_figurinha(figurinha: FigurinhaCreate) -> Figurinha:
    novo_id = max(figurinhas_db.keys(), default=0) + 1
    nova_figurinha = Figurinha(
        id=novo_id,
        nome=figurinha.nome,
        numero=figurinha.numero,
        repetida=figurinha.repetida,
    )
    figurinhas_db[novo_id] = nova_figurinha
    return nova_figurinha


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("mainfast:app", host="0.0.0.0", port=8000, reload=True)
