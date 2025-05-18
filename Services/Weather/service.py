import os
import socket
import requests
from flask import Flask, request, render_template, abort

default_port = 5000
service = "weather"
passphrase = "Louie"
gateway_url = "http://gateway-service:5000/pathway"

ip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__, template_folder="templates")

@app.route(f"/{service}/<secret_key>", methods=["GET", "POST"])
def main_page(secret_key):
    if secret_key != "Gandolf_the_White":
        abort(403)
    weather_info = None
    if request.method == "POST":
        city = request.form.get("city", "").replace(' ', '+')
        resp = requests.get(f"http://wttr.in/{city}?format=3")
        weather_info = resp.text
    return render_template("service.html", key=secret_key, weather=weather_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=default_port)
