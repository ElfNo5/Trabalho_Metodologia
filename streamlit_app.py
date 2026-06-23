"""
Apresentação — Tecnologias Assistivas & Autonomia Plena
=======================================================

App Streamlit que carrega a apresentação (apresentacao.html) e a renderiza
ocupando a tela inteira, mantendo toda a navegação, o estilo "dopamine core /
liquid glass" e os QR codes embutidos.

Rodar localmente:
    pip install -r requirements.txt
    streamlit run streamlit_app.py
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tecnologias Assistivas & Autonomia Plena — Seminário",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Remove o "chrome" do Streamlit e faz a apresentação ocupar a viewport ---
st.markdown(
    """
    <style>
      [data-testid="stHeader"],
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      [data-testid="stStatusWidget"],
      #MainMenu, header, footer { display: none !important; }

      .stApp { background: #000 !important; overflow: hidden !important; }

      .block-container,
      [data-testid="stAppViewContainer"],
      [data-testid="stMain"],
      [data-testid="stMainBlockContainer"] {
          padding: 0 !important;
          margin: 0 !important;
          max-width: 100% !important;
      }

      /* O iframe da apresentação preenche 100% da tela */
      iframe {
          position: fixed !important;
          inset: 0 !important;
          width: 100vw !important;
          height: 100vh !important;
          border: 0 !important;
          z-index: 2147483000 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Carrega e renderiza a apresentação ---
HTML_PATH = Path(__file__).parent / "apresentacao.html"

try:
    deck_html = HTML_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    st.error(
        "Arquivo 'apresentacao.html' não encontrado. "
        "Ele precisa estar na mesma pasta que 'streamlit_app.py'."
    )
    st.stop()

# height é só um fallback; o CSS acima estica o iframe para 100vh.
components.html(deck_html, height=1080, scrolling=False)
