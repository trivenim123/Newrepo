from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from GKE CI/CD mr gopinadh developed own he is leader!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
