import glob
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")
PASTA_SITE = os.path.dirname(PASTA_BASE)


# Todas as 30 imagens estão disponíveis em backend/figurinhas/.
figurinhas = [
    {"id": 1, "nome": "Ayrton Senna", "categoria": "LendasInesqueciveis", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Michael Schumacher", "categoria": "LendasInesqueciveis", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Lewis Hamilton", "categoria": "LendasInesqueciveis", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Alain Prost", "categoria": "LendasInesqueciveis", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Niki Lauda", "categoria": "LendasInesqueciveis", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Max Verstappen", "categoria": "MestresDoGrid", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Fernando Alonso", "categoria": "MestresDoGrid", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Charles Leclerc", "categoria": "MestresDoGrid", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Lando Norris", "categoria": "MestresDoGrid", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "George Russell", "categoria": "MestresDoGrid", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Yuki Tsunoda", "categoria": "NovaGeracao", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Liam Lawson", "categoria": "NovaGeracao", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Oliver Bearman", "categoria": "NovaGeracao", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Andrea Kimi Antonelli", "categoria": "NovaGeracao", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Isack Hadjar", "categoria": "NovaGeracao", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Emerson Fittipaldi", "categoria": "DNAVerdeEAmarelo", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Nelson Piquet", "categoria": "DNAVerdeEAmarelo", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Rubens Barrichello", "categoria": "DNAVerdeEAmarelo", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Felipe Massa", "categoria": "DNAVerdeEAmarelo", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Gabriel Bortoleto", "categoria": "DNAVerdeEAmarelo", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "GP de Interlagos", "categoria": "TemplosEMomentos", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "GP de Monaco", "categoria": "TemplosEMomentos", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "GP de Spa-Francorchamps", "categoria": "TemplosEMomentos", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "A Bandeirada do Título", "categoria": "TemplosEMomentos", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "GP de Silverstone (O Berço da F1)", "categoria": "TemplosEMomentos", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Toto Wolff", "categoria": "MentesBrilhantes", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Christian Horner", "categoria": "MentesBrilhantes", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Adrian Newey", "categoria": "MentesBrilhantes", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Fred Vasseur", "categoria": "MentesBrilhantes", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Ron Dennis", "categoria": "MentesBrilhantes", "imagem_url": "/figurinhas/30/imagem"},
]


@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas


@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinhas(id: int):
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = sorted(glob.glob(padrao))

    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem da figurinha não encontrada")

    return FileResponse(arquivos[0])


# Mantém a demonstração frontend disponível na raiz da aplicação.
app.mount("/", StaticFiles(directory=PASTA_SITE, html=True), name="frontend")
