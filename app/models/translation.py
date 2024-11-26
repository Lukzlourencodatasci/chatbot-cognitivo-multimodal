from transformers import pipeline

# Função para configurar o pipeline de tradução
def get_translator(target_lang):
    if target_lang == "pt":
        return pipeline("text2text-generation", model="Helsinki-NLP/opus-mt-tc-big-en-pt")
    elif target_lang == "en":
        return pipeline("text2text-generation", model="unicamp-dl/translation-pt-en-t5")

# Função para traduzir o texto
def translate_text(text, target_lang):
    translator = get_translator(target_lang)
    prompt = f"translate Portuguese to English: {text}" if target_lang == "en" else f"translate English to Portuguese: {text}"
    result = translator(prompt)
    print(result)  # Verifique a estrutura aqui

    # Tente acessar a chave 'translation_text', mas se falhar, tente outra como 'generated_text'.
    try:
        return result[0]['translation_text']
    except KeyError:
        return result[0]['generated_text']








