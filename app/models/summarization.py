from transformers import pipeline

# Configurar o pipeline de sumarização
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")

def split_text(text, max_length):
    """
    Divide o texto em partes menores com base no comprimento máximo.
    """
    paragraphs = text.split("\n")
    return [p[:max_length] for p in paragraphs if p.strip()]

def summarize_text(text, max_length=1000, min_length=500):
    """
    Sumariza o texto fornecido.

    Args:
        text (str): Texto a ser resumido.
        max_length (int): Comprimento máximo do resumo.
        min_length (int): Comprimento mínimo do resumo.

    Returns:
        str: Resumo gerado.
    """
    input_length = len(text.split())
    adjusted_max_len = min(input_length, max_length)
    adjusted_min_len = min(adjusted_max_len - 1, min_length)

    if input_length > adjusted_max_len:
        paragraphs = split_text(text, adjusted_max_len)
        summaries = []
        for paragraph in paragraphs:
            result = summarizer(paragraph, max_length=adjusted_max_len, min_length=adjusted_min_len, do_sample=False)
            summaries.append(result[0]['summary_text'])
        final_summary = " ".join(summaries)
    else:
        result = summarizer(text, max_length=adjusted_max_len, min_length=adjusted_min_len, do_sample=False)
        final_summary = result[0]['summary_text']

    summary_len = len(final_summary)
    if summary_len < min_length:
        final_summary = summarizer(final_summary, max_length=adjusted_max_len, min_length=min_length, do_sample=False)[0]['summary_text']
    elif summary_len > max_length:
        final_summary = summarizer(final_summary, max_length=max_length, min_length=adjusted_min_len, do_sample=False)[0]['summary_text']

    return final_summary


