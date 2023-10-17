"""
Our API routes live here
"""

from flask import Flask, request
import asyncio

loop = asyncio.get_event_loop()
app = Flask(__name__)


@app.route("/")
def main_page():
    return "Hey There, to use this very specific but soon generic API, use '/generate'"


@app.route("/generate", methods=["POST"])
def generate_text():
    prompt = request.form.get("prompt")
    # Some LLM generation
    results = ""

    return results
