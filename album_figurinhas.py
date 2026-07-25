import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# Define o caminho absoluto da pasta base do projeto
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
# Define a pasta onde as imagens das figurinhas serão armazenadas
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Garante que a pasta de figurinhas exista para o servidor não quebrar
if not os.path.exists(PASTA_IMAGENS):
    os.makedirs(PASTA_IMAGENS)

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Configuração do CORS para o frontend conseguir acessar as figurinhas de qualquer lugar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta a pasta de imagens na rota /imgs para servir arquivos estáticos
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista de figurinhas com os dados e caminho das imagens
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

# Define a rota para o método GET em "/figurinhas"
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas com os links para as imagens
    return figurinhas

if __name__ == "__main__":
    import uvicorn

    # Pega a porta ambiente ou usa 8000 como padrão
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("album_figurinhas:app", host="0.0.0.0", port=port, reload=True)