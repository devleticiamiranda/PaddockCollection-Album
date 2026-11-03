# 🏆 FÓMULA 1- PADDOCK COLECTION

Um álbum de figurinhas digital e interativo que homenageia pioneiros, personalidades e tecnologias que moldaram a história da computação e do desenvolvimento de software.

O projeto recria no navegador a experiência táctil e nostálgica de folhear um álbum físico, combinando animações de física realista, efeitos sonoros sintetizados e integração dinâmica com API backend.

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é apresentar uma aplicação web imersiva e visualmente rica para colecionar figurinhas temáticas de tecnologia. Ele demonstra:
- Estruturação semântica e acessível com **HTML5**.
- Estilização avançada com sombras, profundidade e efeitos visuais modernos via **Vanilla CSS**.
- Interatividade, manipulação de DOM e simulação física de folheio com **JavaScript**.
- Efeitos sonoros gerados dinamicamente via **Web Audio API** (sem dependência de arquivos de áudio externos).
- Consumo assíncrono de dados através de uma **API REST** (FastAPI).

---

## 🚀 Funcionalidades

### 📖 Folheio Realista de Páginas (Flip Book)
- Animação de dobra e virada realista de páginas com sombras 3D proporcionadas pela biblioteca `St.PageFlip`.
- Suporte a **arrastar e puxar a página** com mouse no desktop ou touch em dispositivos móveis.
- Controles de transição inteligente para evitar cliques acidentais e proporcionar uma resposta rápida e suave.

### 🕹️ Controles de Navegação
- **Setas na Interface:** Botões laterais flutuantes para avançar ou retroceder páginas, que se ocultam automaticamente na capa ou na contracapa.
- **Teclado:** Navegação facilitada com as teclas `ArrowLeft` (página anterior) e `ArrowRight` (próxima página).

### 🔊 Síntese Sonora (Web Audio API)
- Geração procedural do som de papel sendo folheado utilizando ruído branco, envelope de volume e filtros passa-banda/passa-baixa.
- **Botão de Som (Mute/Unmute):** Permite silenciar ou reativar o áudio com feedback visual de ícones.


### 🌐 Integração com Backend
- Comunica-se de forma assíncrona (`fetch`) com o endpoint `http://localhost:8000/figurinhas`.
- Identifica os slots existentes via DOM e insere automaticamente a imagem e dados das figurinhas retornadas pelo servidor.
- Aplica estilos visuais distintos (`.slot-preenchido`) quando a figurinha é carregada com sucesso.

---

## 📁 Estrutura de Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| [`index.html`](index.html) | Marcação estrutural do projeto, contendo a capa, páginas temáticas, slots de figurinhas, contracapa e controles de interface. |
| [`style.css`](style.css) | Estilização completa, variáveis de cores (*Tech Blue*, *Deep Blue*), design responsivo e efeitos de acabamento visual. |
| [`app.js`](app.js) | Lógica da aplicação: inicialização do folheio, sintetizador de áudio, atalhos de teclado e requisição para a API. |

---

## 🛠️ Tecnologias Utilizadas

- **HTML5** & **CSS3** (CSS Custom Properties, Flexbox, Grid e Transições)
- **JavaScript (ES6+)** (Async/Await, Web Audio API, Event Listeners)
- **[PageFlip (St.PageFlip)](https://github.com/Nodlik/StPageFlip)**: Biblioteca responsável pelo efeito mecânico de páginas de livro.
- **Google Fonts** (Fontes *Inter* e *Outfit*)

---

## 💻 Como Executar

### 1. Frontend
Basta abrir o arquivo [`index.html`](index.html) em qualquer navegador moderno. Para evitar possíveis bloqueios de CORS ao integrar com a API, recomenda-se utilizar um servidor local (ex: extensão *Live Server* do VS Code ou `npx serve`).

### 2. Backend (Opcional para carregar as imagens das figurinhas)
Caso deseje conectar ao serviço de figurinhas:
```bash
# Exemplo com FastAPI / Uvicorn:
uvicorn main:app --reload --port 8000
```
> **Nota:** Caso o backend não esteja ativo, o álbum continuará funcionando normalmente com seus efeitos visuais e slots em modo placeholder.
