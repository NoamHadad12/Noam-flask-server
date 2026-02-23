from flask import Flask, render_template_string

app = Flask(__name__)

# Modern HTML template with Tailwind CSS for a "cool" look
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Noam Hadad - Personal Site</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #0f172a; color: white; font-family: sans-serif; }
        .hero-gradient { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); }
    </style>
</head>
<body class="min-h-screen flex flex-col items-center justify-center p-6">
    <div class="max-w-3xl w-full bg-slate-800 rounded-3xl shadow-2xl overflow-hidden border border-slate-700">
        <div class="hero-gradient p-12 text-center">
            <h1 class="text-5xl font-extrabold mb-4 tracking-tight">Noam Hadad</h1>
            <p class="text-xl opacity-90">CS Student | AI Enthusiast | Football & NBA Fan</p>
        </div>

        <div class="p-8 space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="bg-slate-700 p-4 rounded-xl border border-slate-600">
                    <h3 class="font-bold text-blue-400 mb-2">Education</h3>
                    <p class="text-sm">3rd Year Computer Science Student at JCT</p>
                </div>
                <div class="bg-slate-700 p-4 rounded-xl border border-slate-600">
                    <h3 class="font-bold text-blue-400 mb-2">Projects</h3>
                    <p class="text-sm italic">"HoneyCipher" Honeypot System & More</p>
                </div>
            </div>

            <div class="text-center space-y-4 pt-4">
                <p class="text-slate-400">Try my API endpoints:</p>
                <div class="flex justify-center gap-4">
                    <a href="/Noam" class="px-6 py-2 bg-blue-600 hover:bg-blue-500 rounded-full transition font-semibold">Greet Noam</a>
                    <a href="/Hadad" class="px-6 py-2 bg-slate-600 hover:bg-slate-500 rounded-full transition font-semibold">Full Name</a>
                </div>
            </div>
        </div>

        <footer class="p-4 bg-slate-900 text-center text-xs text-slate-500 uppercase tracking-widest">
            Built with Flask & Deployed on Render
        </footer>
    </div>
</body>
</html>
"""


# Home Route - The "Cool" Website
@app.route("/")
def index():
    # Returns the designed HTML page
    return render_template_string(HTML_TEMPLATE)


# Route for the '/Noam' endpoint
@app.get("/Noam")
def home():
    # Simple plain text response
    return "Hello Noam!"


# Route for the '/Hadad' endpoint
@app.get("/Hadad")
def home1():
    # Response with the full surname
    return "Hello Noam Hadad!"


if __name__ == "__main__":
    # Ensure the server listens on all interfaces for Docker/Cloud compatibility
    app.run(host="0.0.0.0", port=8000)