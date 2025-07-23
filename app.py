from flask import Flask, render_template
from datetime import date
import os

app = Flask(__name__)

# Daily rotating quotes
quotes = [
    "“If dogs wore pants, would they bark in lowercase?”",
    "“Reality is just improv without a stage.”",
    "“The only thing more broken than my sleep schedule is this meme.”"
]

# Matching meme image URLs
memes = [
    "https://i.imgur.com/zYR5plL.jpg",
    "https://i.imgur.com/LJmHQDJ.jpg",
    "https://i.imgur.com/ZcNtxpS.jpg"
]

@app.route("/")
def home():
    index = date.today().toordinal() % len(quotes)
    quote = quotes[index]
    meme = memes[index]
    return render_template("index.html", quote=quote, meme=meme)

# ✅ This is the key fix for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
