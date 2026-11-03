# 🏎️ Fórmula 1 — Paddock Collection

Álbum digital interativo de figurinhas inspirado na Fórmula 1. O projeto apresenta pilotos, circuitos, estrategistas e momentos marcantes do automobilismo em uma experiência visual de álbum físico, com páginas animadas e integração entre frontend e backend.

## 🏁 Sobre o projeto

O objetivo é demonstrar, de forma prática, como uma aplicação web pode separar responsabilidades entre:

- 🎨 **Frontend:** interface, animações, navegação e montagem visual do álbum.
- ⚙️ **Backend:** catálogo das figurinhas, categorias, CORS e entrega das imagens por API.

O álbum possui 30 figurinhas distribuídas em categorias temáticas, com imagens servidas pelo backend através de endpoints próprios.

## ✨ Funcionalidades

- 🏎️ Álbum interativo de Fórmula 1 com capa, contracapa e efeito de folheio.
- 🃏 Catálogo com 30 figurinhas, categorias e imagens organizadas por ID.
- 🔄 Integração entre frontend JavaScript e API REST em FastAPI.
- 🖼️ Endpoint próprio para entrega das imagens das figurinhas.
- 📱 Layout responsivo com navegação por setas, teclado e arraste.

## 🛠️ Tecnologias utilizadas

### 🎨 Frontend

-  HTML5
-  CSS3
-  JavaScript ES6+
-  CSS Grid e Flexbox
-  SVG para elementos visuais
-  Google Fonts: Inter e Outfit
- [St.PageFlip](https://github.com/Nodlik/StPageFlip)

### ⚙️ Backend

-  Python
-  FastAPI
-  Uvicorn
-  `fastapi.middleware.cors.CORSMiddleware`
-  `glob` para localizar as imagens por ID

### 🤖 Inteligência Artificial

A Inteligência Artificial foi utilizada como apoio no processo criativo e visual do projeto, especialmente para referências e exploração da identidade visual da capa, contracapa e elementos relacionados à Fórmula 1. A aplicação não depende de um modelo de IA para funcionar em tempo de execução.

## 📁 Estrutura do projeto

```text
ArquiteturaWeb/
├── index.html                 # Estrutura do álbum e suas páginas
├── style.css                  # Estilos, grids, capa, contracapa e responsividade
├── app.js                     # Navegação, PageFlip e integração com a API
├── README.md                  # Documentação do projeto
├── assets/
│   ├── f1-logo.png            # Logo utilizada na capa e contracapa
│   └── senna-helmet.jpg       # Capacete utilizado na capa
└── backend/
    ├── main.py                # Aplicação FastAPI
    ├── requirements.txt       # Dependências Python
    └── figurinhas/            # 30 imagens das figurinhas
        ├── 01-ayrtonsenna.jpg
        ├── 02-michaelschumacher.jpg
        └── ...
```

## ▶️ Como executar localmente

### 1️⃣ Criar ou ativar um ambiente virtual

Na pasta do projeto:

```bash
python -m venv backend/.venv
```

No Windows PowerShell:

```powershell
backend\.venv\Scripts\Activate.ps1
```

### 2️⃣ Instalar as dependências

```bash
pip install -r backend/requirements.txt
```

### 3️⃣ Iniciar o backend

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Depois, acesse:

```text
http://127.0.0.1:8000/
```

## 🔌 Endpoints da API

### 🃏 Listar figurinhas

```http
GET /figurinhas
```

Retorna a lista das 30 figurinhas com seus respectivos IDs, nomes, categorias e URLs de imagem.

### 🖼️ Obter imagem por ID

```http
GET /figurinhas/{id}/imagem
```

Exemplo:

```text
http://127.0.0.1:8000/figurinhas/1/imagem
```

O backend localiza o arquivo cujo nome começa com o ID de dois dígitos, como `01-ayrtonsenna.jpg`.

## 🚀 Observações para publicação

O GitHub armazena o código, mas não executa o servidor FastAPI. Para colocar a aplicação online, é necessário:

- Hospedar o frontend em um serviço estático, como GitHub Pages.
- Hospedar o backend em um serviço Python, como Render, Railway, Fly.io ou AWS.
- Configurar a URL pública da API no frontend quando frontend e backend estiverem em domínios diferentes.

O ambiente virtual `.venv`, a pasta `__pycache__` e arquivos `.pyc` não devem ser enviados ao repositório. As dependências são reproduzidas pelo arquivo `backend/requirements.txt`.

## 👩‍💻 Autora

Desenvolvido por **Letícia Miranda**.

