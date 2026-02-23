from flask import Flask, render_template_string

app = Flask(__name__)

# Modern HTML and CSS (Tailwind) for your portfolio site
# Using English comments as per your request
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Noam Hadad - Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white font-sans min-h-screen flex items-center justify-center">
    <div class="text-center p-10 bg-slate-800 rounded-3xl shadow-2xl border border-slate-700 max-w-lg">
        <h1 class="text-5xl font-extrabold text-blue-400 mb-4">Noam Hadad</h1>
        <p class="text-xl text-slate-300 mb-6 italic">3rd Year CS Student @ JCT | Software Developer</p>

        <div class="space-y-4">
            <p class="text-slate-400">Welcome to my live server! Check out my API endpoints:</p>
            <div class="flex justify-center gap-4">
                <a href="/Noam" class="bg-blue-600 hover:bg-blue-500 px-6 py-2 rounded-full font-bold transition">Greet Me</a>
                <a href="/Hadad" class="bg-slate-700 hover:bg-slate-600 px-6 py-2 rounded-full font-bold transition">Full Name</a>
            </div>
        </div>

        <div class="mt-10 pt-6 border-t border-slate-700">
            <p class="text-xs text-slate-500 uppercase tracking-widest">Active Projects: HoneyCipher</p>
        </div>
    </div>
</body>
</html>
"""


# The Root Route - This is what your friends will see at the main URL
@app.route("/")
def index():
    # Returns the professional HTML design
    return render_template_string(HTML_CONTENT)


# Existing endpoints
@app.get("/Noam")
def home():
    return "Hello Noam!"


@app.get("/Hadad")
def home1():
    return "Hello Noam Hadad!"


if __name__ == "__main__":
    # Required host 0.0.0.0 for Render accessibility
    app.run(host="0.0.0.0", port=8000)