from transformers import pipeline

# Configurar o pipeline para sumarização (usando um modelo robusto)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")

def summarize_text(text, max_length=1000, min_length=500):
    # Verifique o comprimento do texto
    input_length = len(text.split())  # Número de palavras no texto
    
    # Ajuste dinâmico de max_length e min_length com base no comprimento do texto
    adjusted_max_len = min(input_length, max_length)  # Ajusta max_length com base no tamanho do texto
    adjusted_min_len = min(adjusted_max_len - 1, min_length)  # Ajusta min_length para ser menor que max_length

    # Caso o texto seja longo, divida em blocos menores para o modelo lidar melhor com a entrada
    if input_length > adjusted_max_len:
        paragraphs = text.split("\n")  # Divida por parágrafos ou por outras lógicas
        summaries = []
        
        for paragraph in paragraphs:
            if len(paragraph.strip()) > 0:  # Ignorar parágrafos vazios
                # Aplique a sumarização ao parágrafo
                result = summarizer(paragraph, max_length=adjusted_max_len, min_length=adjusted_min_len, do_sample=False)
                summaries.append(result[0]['summary_text'])
        
        # Juntar os resumos em um único resumo final
        final_summary = " ".join(summaries)
    else:
        # Caso o texto seja pequeno o suficiente, sumarize-o diretamente
        result = summarizer(text, max_length=adjusted_max_len, min_length=adjusted_min_len, do_sample=False)
        final_summary = result[0]['summary_text']

    # Garantir que o resumo final esteja dentro do limite de caracteres
    summary_len = len(final_summary)

    # Ajuste se o resumo for muito curto ou longo
    if summary_len < min_length:
        final_summary = summarizer(final_summary, max_length=adjusted_max_len, min_length=min_length, do_sample=False)[0]['summary_text']
    elif summary_len > max_length:
        final_summary = summarizer(final_summary, max_length=max_length, min_length=adjusted_min_len, do_sample=False)[0]['summary_text']

    return final_summary



