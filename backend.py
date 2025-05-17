from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return '<h1>Welcome to the backend</h1>'

@app.route("/secure")
def flag():
    return '<h1>Welcome troublemaker</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
