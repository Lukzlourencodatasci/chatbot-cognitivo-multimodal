import streamlit as st
import os
from models.translation import translate_text
from models.summarization import summarize_text
from models.image_gen import generate_image

# Configuração inicial
st.set_page_config(page_title="GPTurbo Cognitivo Multimodal Deluxe", layout="wide")

# CSS Customizado para Estilo
st.markdown("""
    <style>
    .stApp {
        background-color: #1E3A5F;
        color: #F0F8FF;
    }
    .title {
        font-size: 40px;
        color: #FFFFFF;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }
    div[data-testid="stHorizontalBlock"] > div:first-child {
        background-color: #324A72;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
    }
    textarea, input {
        background-color: #FFFFFF !important;
        color: #1E3A5F !important;
        border: 1px solid #61dafb !important;
    }
    label, .css-16huue1, .css-qrbaxs {
        color: #FFFFFF !important; /* Torna os textos em branco */
    }
    button {
        background-color: #3B5998 !important;
        color: #FFFFFF !important;
        border-radius: 5px;
        padding: 10px;
    }
    button:hover {
        background-color: #1E90FF !important;
    }
    .output-box {
        padding: 10px;
        background-color: #FFFFFF;
        color: #1E3A5F;
        border: 1px solid #61dafb;
        border-radius: 5px;
        margin-top: 10px;
        width: 100%;
        word-wrap: break-word;
    }
    </style>
""", unsafe_allow_html=True)

# Caminho absoluto da imagem
image_path = os.path.join(os.getcwd(), "app", "images", "organizacoes-tabajara.png")

# Cabeçalho com Imagem e Título
st.markdown("<div class='header-container'>", unsafe_allow_html=True)
st.image(image_path, width=150)
st.markdown("<h1 class='title'>GPTurbo Cognitivo Multimodal Deluxe</h1></div>", unsafe_allow_html=True)

# Layout Moderno com Abas
tab1, tab2, tab3 = st.tabs(["🌐 Tradução", "📜 Sumarização", "🎨 Criação de Imagens"])

# Funcionalidade de Tradução
with tab1:
    st.subheader("Tradução")
    col1, col2 = st.columns([2, 1])
    with col1:
        text_translation = st.text_area("Insira o texto para tradução:")
    with col2:
        lang = st.selectbox("Idioma de destino:", ["en", "pt"], key="translation_lang")
    if st.button("Traduzir", key="translate_button"):
        with st.spinner("Traduzindo..."):
            try:
                result = translate_text(text_translation, lang)
                st.markdown(f"<div class='output-box'>{result}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erro durante a tradução: {e}")

# Funcionalidade de Sumarização
with tab2:
    st.subheader("Sumarização")
    col1, col2 = st.columns([2, 1])
    with col1:
        text_summary = st.text_area("Insira o texto para sumarização:")
    with col2:
        max_len = st.slider("Comprimento máximo (em caracteres):", 500, 1000, 1000, key="max_len_slider")
        min_len = st.slider("Comprimento mínimo (em caracteres):", 500, 1000, 500, key="min_len_slider")
    if st.button("Resumir", key="summarize_button"):
        with st.spinner("Resumindo..."):
            try:
                result = summarize_text(text_summary, max_length=max_len, min_length=min_len)
                st.markdown(f"<div class='output-box'>{result}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erro durante a sumarização: {e}")

# Funcionalidade de Criação de Imagens
with tab3:
    st.subheader("Criação de Imagens")
    col1, col2 = st.columns([2, 1])
    with col1:
        description = st.text_input("Digite a descrição da imagem (máx. 100 caracteres):", key="image_description")
    with col2:
        if st.button("Gerar Imagem", key="generate_image_button"):
            with st.spinner("Gerando imagem..."):
                try:
                    image = generate_image(description)
                    st.image(image, caption="Imagem gerada", use_column_width=True)
                except Exception as e:
                    st.error(f"Erro ao gerar imagem: {e}")
