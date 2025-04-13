from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def abstractive_summary(text, min_len=10):
    input_length = len(text.split())
    max_len = min(max(int(input_length * 0.8), min_len + 5), 120)  # Adjust for smaller inputs
    if input_length < min_len:
        return text
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']