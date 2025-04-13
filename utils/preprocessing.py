import re
from bs4 import BeautifulSoup


def clean_text(text):
    # Remove HTML
    text = BeautifulSoup(text, "html.parser").get_text()
    # Remove unwanted characters
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s\.\,]", "", text)
    return text.strip()
