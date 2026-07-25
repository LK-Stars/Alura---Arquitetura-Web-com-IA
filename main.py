from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

# Define o caminho absoluto da pasta base do projeto
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
# Define a pasta onde as imagens das figurinhas serão armazenadas
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

app = FastAPI()

# Monta a pasta de imagens na rota /imgs para servir arquivos estáticos
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista de figurinhas disponíveis na API
figurinhas = [
    {
        "id": 1,
        "nome": "Alan Turing",
        "categoria": "IA",
        "imagem_url": "/imgs/01-alan-turing.jpg",
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/imgs/02-john-mccarthy.jpg",
    },
]


# Endpoint para listar todas as figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
