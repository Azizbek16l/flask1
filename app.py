from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "salom dev"


if __name__ == "__main__":
    app.run(port=4200, debug=False)
