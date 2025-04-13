# Text Summarization Project

This project provides **extractive** and **abstractive** summaries of articles using Python NLP libraries and a Flask web interface.

## Features

- **Extractive Summarization using LSA (Sumy)**  
  Uses the **Latent Semantic Analysis (LSA)** algorithm to extract important sentences from the article. This method focuses on identifying key sentences based on their relevance to the overall content.

- **Abstractive Summarization using BART (Hugging Face)**  
  Utilizes the **BART model** from **Hugging Face** to generate new, concise summaries by interpreting and rewriting the content. The model produces summaries that may not be directly present in the original text.

- **Text Preprocessing (HTML cleaning, regex)**  
  Cleans the input text by removing unnecessary HTML tags, whitespace, and non-alphanumeric characters. It ensures the text is in a clean format for summarization.

- **Dynamic Summary Length adjusted based on input size**  
  The length of the generated summary is dynamically adjusted based on the input text's length, ensuring a relevant summary that is neither too short nor too long.

- **Web Interface built with Flask**  
  Provides an easy-to-use web interface where users can paste articles, select the type of summarization, and view or download the generated summaries.

- **Summaries saved as text files**  
  After summarizing the article, the summaries are saved as separate text files on the local system for easy access and download.

## Technologies

- **Python** for development.  
  Python serves as the core programming language, providing flexibility and compatibility with numerous NLP and web frameworks.

- **Sumy for extractive summarization (LSA)**  
  **Sumy** is a Python library that implements various extractive summarization techniques, including **LSA**, making it easy to pull out key sentences from text.

- **Hugging Face Transformers for abstractive summarization (BART)**  
  The **Hugging Face Transformers** library provides pre-trained models like **BART** to generate human-like summaries by rephrasing the input content.

- **Flask for the web UI**  
  **Flask** is a lightweight web framework used to create a simple and intuitive web interface for summarization tasks, allowing users to interact with the system through their browser.

- **NLTK and BeautifulSoup for text processing**  
  **NLTK** helps with tokenization and other NLP tasks, while **BeautifulSoup** is used for cleaning and extracting text from HTML documents.
