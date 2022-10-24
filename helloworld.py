from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello, ElbowAI Gurus!"


# define our routes
@app.route("/api/v1/predict")
def elbow():
    return {"age": 30, "income": 40000, "height": 165, "credit_score": 700}


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=1957, debug=True)
