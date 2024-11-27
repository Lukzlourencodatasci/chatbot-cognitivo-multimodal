from transformers import MBartForConditionalGeneration, MBart50Tokenizer

# Configurar o modelo e o tokenizer para o mBART
model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBart50Tokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

# Configurar o idioma-alvo no tokenizer
LANGUAGE_CODES = {
    "en": "en_XX",  # Código para inglês
    "pt": "pt_XX",  # Código para português
}

def translate_text(text, target_lang, max_length=512):
    """
    Traduz o texto para o idioma de destino usando mBART.

    Args:
        text (str): Texto a ser traduzido.
        target_lang (str): Idioma de destino ("en" ou "pt").
        max_length (int): Comprimento máximo do texto.

    Returns:
        str: Texto traduzido.
    """
    if target_lang not in LANGUAGE_CODES:
        raise ValueError("Idioma de destino inválido. Use 'en' ou 'pt'.")

    # Cortar o texto se exceder o comprimento máximo
    text = text[:max_length]

    # Tokenizar o texto de entrada e definir o idioma de destino
    tokenizer.src_lang = LANGUAGE_CODES["pt"] if target_lang == "en" else LANGUAGE_CODES["en"]
    encoded_text = tokenizer(text, return_tensors="pt", max_length=max_length, truncation=True)

    # Gerar a tradução
    translated_tokens = model.generate(
        **encoded_text,
        forced_bos_token_id=tokenizer.lang_code_to_id[LANGUAGE_CODES[target_lang]],
        max_length=max_length
    )

    # Decodificar o texto traduzido
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text








