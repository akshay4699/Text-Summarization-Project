import warnings
warnings.filterwarnings("ignore")

from models.extractive_summarizer import extractive_summary
from models.abstractive_summarizer import abstractive_summary
from utils.preprocessing import clean_text

if __name__ == "__main__":
    with open("data/article1.txt", "r", encoding="utf-8") as file:
        text = file.read()

    cleaned = clean_text(text)

    extractive = extractive_summary(cleaned)
    abstractive = abstractive_summary(cleaned)

    print("\n--- Extractive Summary ---\n")
    print(extractive)

    print("\n--- Abstractive Summary ---\n")
    print(abstractive)

    with open("data/extractive_summary.txt", "w", encoding="utf-8") as out1:
        out1.write(extractive)

    with open("data/abstractive_summary.txt", "w", encoding="utf-8") as out2:
        out2.write(abstractive)
