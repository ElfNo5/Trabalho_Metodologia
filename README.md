# Tecnologias Assistivas & Autonomia Plena — Seminário

Apresentação interativa (HTML + estilo *dopamine core / liquid glass*) sobre
**a falta de acessibilidade para pessoas com deficiência visual na sociedade
brasileira no contexto das tecnologias de sistemas inteligentes**, empacotada
como um app **Streamlit** em Python — pronta para o GitHub e o Streamlit Cloud.

A navegação, os efeitos de vidro e os **QR codes dos artigos** já estão embutidos
no arquivo `apresentacao.html`; o Streamlit apenas o exibe em tela cheia.

---

## 📁 Estrutura do projeto

```
.
├── streamlit_app.py        # app Streamlit (carrega e exibe a apresentação)
├── apresentacao.html       # a apresentação em si (auto-contida)
├── requirements.txt        # dependências (apenas streamlit)
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml         # tema escuro
```

---

## ▶️ Rodar localmente

Pré-requisito: Python 3.9+.

```bash
# 1. (opcional) crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. instale as dependências
pip install -r requirements.txt

# 3. rode
streamlit run streamlit_app.py
```

O navegador abre em `http://localhost:8501`.

---

## ☁️ Publicar no Streamlit Community Cloud (grátis)

1. Crie um repositório no **GitHub** e suba estes arquivos:
   ```bash
   git init
   git add .
   git commit -m "Apresentação Tecnologias Assistivas"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
   git push -u origin main
   ```
2. Acesse **https://share.streamlit.io** e faça login com o GitHub.
3. Clique em **Create app** → selecione o repositório, o branch `main` e o
   arquivo principal **`streamlit_app.py`**.
4. Clique em **Deploy**. Em ~1 min você terá um link público da apresentação.

---

## ⌨️ Como apresentar

- **→ / Espaço** — avança (revela tópico a tópico e depois muda de slide)
- **←** — volta
- **Home / End** — primeiro / último slide
- Botões **‹ ›** no canto inferior direito (funcionam só com o mouse)
- **Clique uma vez na apresentação** para que as setas do teclado funcionem
  (o conteúdo roda dentro de um iframe e precisa receber o foco).
- Para tela cheia de verdade no navegador, use **F11** (o atalho `F` interno
  pode ser bloqueado dentro do Streamlit).

---

## 🔗 QR codes

Os 8 QR codes dos artigos **e** o QR do documento da pesquisa já estão gerados e
embutidos como imagem dentro do `apresentacao.html` — funcionam **offline** e
foram validados.

- O QR do **documento** aponta para o link do Google Docs fornecido. Confirme que
  o compartilhamento está como **"qualquer pessoa com o link pode ver"**, senão
  quem escanear não conseguirá abrir.
- Para **trocar algum link/QR**, é mais simples regenerar — me peça que eu gero o
  novo `apresentacao.html`.

---

## ✏️ Editar o conteúdo

Todo o conteúdo (textos, cores, slides) está em `apresentacao.html`. Pode editar
direto e dar `git push`; o Streamlit Cloud atualiza sozinho a cada commit.

> Observação: as fontes (Google Fonts) carregam pela internet. Em apresentações
> sem rede, o navegador usa fontes de fallback automaticamente — o layout
> continua funcionando.
