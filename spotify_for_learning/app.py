from flask import Flask, render_template, request, send_file
from backend import create_audio_snippet
import os

app = Flask(__name__)
AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    display_text = None
    if request.method == "POST":
        topics = request.form.get("topics")
        time_limit = int(request.form.get("time_limit", 5))
        audio_file, display_text = create_audio_snippet(topics, time_limit, AUDIO_DIR)
    return render_template("index.html", audio_file=audio_file, display_text=display_text)

if __name__ == "__main__":
    app.run(debug=True)
