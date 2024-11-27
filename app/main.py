'''import streamlit as st
from models.translation import translate_text
from models.summarization import summarize_text  # Importa a função de sumarização
from transformers import pipeline

st.title("ChatBot Cognitivo Multimodal")

# Sidebar para funcionalidades
option = st.sidebar.selectbox("Escolha uma funcionalidade:", 
                               ["Tradução", "Sumarização", "Criação de Imagens"])

# Funcionalidade de Tradução
if option == "Tradução":
    text = st.text_area("Insira o texto para tradução:")
    lang = st.selectbox("Idioma de destino:", ["en", "pt"])
    if st.button("Traduzir"):
        result = translate_text(text, lang)
        st.write("Tradução:", result)

# Funcionalidade de Sumarização
elif option == "Sumarização":
    st.title("Aplicação de Sumarização de Texto")  # Título para a parte de sumarização
    text = st.text_area("Insira o texto para sumarização:")

    # Definindo os limites de comprimento
    max_len = st.slider("Comprimento máximo (em caracteres):", 500, 1000, 1000)
    min_len = st.slider("Comprimento mínimo (em caracteres):", 500, 1000, 500)

    if st.button("Resumir"):
        # Chama a função de sumarização com os parâmetros definidos
        result = summarize_text(text, max_length=max_len, min_length=min_len)
        st.write("Resumo:", result)

# Funcionalidade de Criação de Imagens
elif option == "Criação de Imagens":
    st.write("Em breve: funcionalidade de criação de imagens!")
    
# Se nenhuma opção for selecionada, exibe uma mensagem padrão.
else:
    st.write("Escolha uma funcionalidade para começar.")'''

import streamlit as st
from models.translation import translate_text
from models.summarization import summarize_text
from models.image_gen import generate_image

st.title("ChatBot Cognitivo Multimodal")

# Tabs para facilitar a navegação
tabs = st.tabs(["Tradução", "Sumarização", "Criação de Imagens"])

# Funcionalidade de Tradução
with tabs[0]:
    st.header("Tradução")
    text_translation = st.text_area("Insira o texto para tradução:")
    lang = st.selectbox("Idioma de destino:", ["en", "pt"], key="translation_lang")
    if st.button("Traduzir", key="translate_button"):
        with st.spinner("Traduzindo..."):
            try:
                result = translate_text(text_translation, lang)
                st.write("Tradução:", result)
            except Exception as e:
                st.error(f"Erro durante a tradução: {e}")

# Funcionalidade de Sumarização
with tabs[1]:
    st.header("Sumarização")
    text_summary = st.text_area("Insira o texto para sumarização:")
    max_len = st.slider("Comprimento máximo (em caracteres):", 500, 1000, 1000, key="max_len_slider")
    min_len = st.slider("Comprimento mínimo (em caracteres):", 500, 1000, 500, key="min_len_slider")

    if st.button("Resumir", key="summarize_button"):
        with st.spinner("Resumindo..."):
            try:
                result = summarize_text(text_summary, max_length=max_len, min_length=min_len)
                st.write("Resumo:", result)
            except Exception as e:
                st.error(f"Erro durante a sumarização: {e}")

# Funcionalidade de Criação de Imagens
with tabs[2]:
    st.header("Criação de Imagens")
    description = st.text_input("Digite a descrição da imagem (máx. 100 caracteres):", key="image_description")
    if st.button("Gerar Imagem", key="generate_image_button"):
        with st.spinner("Gerando imagem..."):
            try:
                image = generate_image(description)
                st.image(image, caption="Imagem gerada", use_column_width=True)
            except Exception as e:
                st.error(f"Erro ao gerar imagem: {e}")
