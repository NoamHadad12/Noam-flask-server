import os
from flask import Flask, render_template_string

app = Flask(__name__)

# [Content of HTML_CONTENT variable omitted for brevity, assuming existing content]
HTML_CONTENT = """..."""  # (Existing HTML content)

# The Root Route - Renders the upgraded template
@app.route("/")
def index():
    return render_template_string(HTML_CONTENT)

# Existing endpoints as requested
@app.get("/Noam")
def home():
    return "Hello Noam! (The GOAT)"

@app.get("/Hadad")
def home1():
    return "Hello Noam Hadad! (Supreme Developer)"

if __name__ == "__main__":
    # Apply Bonus 1: Remove hardcoded port, use environment variable
    # This allows the hosting platform (like Render) to inject the correct port
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)