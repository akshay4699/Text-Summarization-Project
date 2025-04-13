# app/flask_app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, render_template
from models.extractive_summarizer import extractive_summary
from models.abstractive_summarizer import abstractive_summary
from utils.preprocessing import clean_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        raw_text = request.form.get("article")
        summary_type = request.form.get("summary_type")
        cleaned = clean_text(raw_text)
        if summary_type == "Extractive":
            summary = extractive_summary(cleaned)
        else:
            summary = abstractive_summary(cleaned)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
