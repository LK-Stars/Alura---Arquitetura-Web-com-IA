from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

app = FastAPI()

@app.get("/")
def pagina_inicial():
    return {
        "status": "API do Álbum de Figurinhas Rodando com Sucesso!",
        "mensagem": "Olá, mundo! 🌍",
        "dica": "Acesse /figurinhas para ver a lista ou /docs para testar os recursos."
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Sam", "categoria": "IA", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Geoffrey", "categoria": "IA", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Yann", "categoria": "IA", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Guido", "categoria": "Simplicidade", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Tim", "categoria": "Simplicidade", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Ray", "categoria": "Simplicidade", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Travis", "categoria": "Simplicidade", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Wes", "categoria": "Simplicidade", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Edgar", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Larry", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Michael", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Salvatore", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Eliot", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Linus", "categoria": "Computação Moderna", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Dennis", "categoria": "Computação Moderna", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Richard", "categoria": "Computação Moderna", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Bill", "categoria": "Computação Moderna", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Steve", "categoria": "Computação Moderna", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Paulo", "categoria": "Celebridades Tech - Vol 1", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Guilherme", "categoria": "Celebridades Tech - Vol 1", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Gus", "categoria": "Celebridades Tech - Vol 1", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Mauricio", "categoria": "Celebridades Tech - Vol 1", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Andre", "categoria": "Celebridades Tech - Vol 1", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Guilherme", "categoria": "Celebridades Tech - Vol 2", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Gi", "categoria": "Celebridades Tech - Vol 2", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Vinicius", "categoria": "Celebridades Tech - Vol 2", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Rafa", "categoria": "Celebridades Tech - Vol 2", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "LK", "categoria": "Celebridades Tech - Vol 2", "imagem_url": "/figurinhas/30/imagem"},
    # Figurinhas adicionais não disponíveis ainda podem ser adicionadas aqui.
]

@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

@app.get("/figurinhas/{id}/imagem")
def imagem_figurinha(id: int):
    pattern = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(pattern)

    if not arquivos:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada")

    arquivo = sorted(arquivos)[0]
    return FileResponse(arquivo)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9001)
