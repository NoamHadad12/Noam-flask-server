from flask import Flask, render_template_string

app = Flask(__name__)

# Updated HTML content with "Legendary" status, animations, and glorification
# Using English comments strictly
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Legend: Noam Hadad</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom animations for the 'cool' factor */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }
        @keyframes glow {
            0% { text-shadow: 0 0 10px #3b82f6, 0 0 20px #3b82f6; }
            50% { text-shadow: 0 0 20px #60a5fa, 0 0 40px #60a5fa; }
            100% { text-shadow: 0 0 10px #3b82f6, 0 0 20px #3b82f6; }
        }
        .animate-float {
            animation: float 6s ease-in-out infinite;
        }
        .animate-glow {
            animation: glow 3s ease-in-out infinite;
        }
        .glass-panel {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(10px);
        }
    </style>
</head>
<body class="bg-slate-950 text-white font-sans min-h-screen flex flex-col items-center justify-center overflow-hidden relative">

    <div class="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <div class="absolute top-[-10%] left-[-10%] w-96 h-96 bg-blue-600 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob"></div>
        <div class="absolute top-[-10%] right-[-10%] w-96 h-96 bg-purple-600 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-2000"></div>
        <div class="absolute bottom-[-20%] left-[20%] w-96 h-96 bg-pink-600 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-4000"></div>
    </div>

    <div class="glass-panel text-center p-12 rounded-3xl shadow-2xl border border-slate-700 max-w-2xl transform hover:scale-105 transition duration-500">

        <h1 class="text-7xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 mb-2 animate-glow">
            NOAM HADAD
        </h1>
        <p class="text-2xl text-blue-200 mb-8 font-light tracking-widest uppercase">The Myth. The Legend. The Compile Master.</p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-left mb-10">
            <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700 hover:border-blue-500 transition">
                <h3 class="text-xl font-bold text-blue-400 mb-2">💻 CS Prodigy</h3>
                <p class="text-slate-300 text-sm">JCT doesn't teach Noam; Noam teaches the curriculum. Python bows down when he opens his IDE.</p>
            </div>
            <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700 hover:border-purple-500 transition">
                <h3 class="text-xl font-bold text-purple-400 mb-2">⚽ Football Icon</h3>
                <p class="text-slate-300 text-sm">Scouts from Europe are calling. He plays in Rehovot just to give the others a fair chance.</p>
            </div>
            <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700 hover:border-pink-500 transition">
                <h3 class="text-xl font-bold text-pink-400 mb-2">🛡️ Cyber Warlord</h3>
                <p class="text-slate-300 text-sm">Creator of <strong>HoneyCipher</strong>. Hackers see his firewall and immediately apologize.</p>
            </div>
            <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700 hover:border-green-500 transition">
                <h3 class="text-xl font-bold text-green-400 mb-2">👔 Style God</h3>
                <p class="text-slate-300 text-sm">Size 34, fit perfection. When he buys sneakers, the price goes up.</p>
            </div>
        </div>

        <div class="space-y-6">
            <p class="text-slate-400 italic">"I don't deploy code, I release greatness."</p>
            <div class="flex justify-center gap-6">
                <a href="/Noam" class="relative inline-flex items-center justify-center px-8 py-3 overflow-hidden font-bold text-white transition-all duration-300 bg-blue-600 rounded-full group hover:bg-blue-500 hover:ring-2 hover:ring-blue-400 hover:ring-offset-2 hover:ring-offset-slate-900">
                    <span class="absolute transition-all duration-300 origin-center rotate-45 -translate-x-20 bg-white opacity-10 group-hover:translate-x-32 group-hover:-translate-y-32 w-32 h-64"></span>
                    <span class="relative">Witness Greatness</span>
                </a>
                <a href="/Hadad" class="relative inline-flex items-center justify-center px-8 py-3 overflow-hidden font-bold text-white transition-all duration-300 bg-slate-700 rounded-full group hover:bg-slate-600">
                     <span class="relative">Say My Name</span>
                </a>
            </div>
        </div>
    </div>

    <footer class="absolute bottom-4 text-slate-600 text-xs">
        Powered by pure talent & a bit of Flask
    </footer>
</body>
</html>
"""


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
    # Required host configuration for external access
    app.run(host="0.0.0.0", port=8000)