from flask import Flask

app = Flask(__name__)

# Route for the '/Noam' endpoint
@app.get("/Noam")
def home():
    return "Hello Noam!"

# Route for the '/Hadad' endpoint
@app.get("/Hadad")
def home1():
    return "Hello Noam Hadad!"

# Main block to run the server
if __name__ == "__main__":
    # Host 0.0.0.0 makes the server accessible on the local network
    # Port 8000 is the specific port the server listens to
    app.run(host="0.0.0.0", port=8000)

