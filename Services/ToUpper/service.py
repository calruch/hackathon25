import os
import socket
import requests
from flask import Flask, request, render_template, abort

default_port = 5000
service = "to-upper"
passphrase = "Huey"
gateway_url = "http://gateway-service:5000/pathway"

ip = socket.gethostbyname(socket.gethostname())

requests.post(
    gateway_url,
    headers={"passphrase": passphrase},
    data={"service": service, "ip": ip}
)

app = Flask(__name__, template_folder="templates")

@app.route(f"/{service}/<secret_key>", methods=["GET", "POST"])
def main_page(secret_key):
    if secret_key != "Gandolf_the_White":
        abort(403)
    result = None
    if request.method == "POST":
        text = request.form.get("text", "")
        result = text.upper()
    return render_template("service.html", key=secret_key, result=result)

# (Original Code)
# @app.route("/upper/<echo_string>")
# def upper(echo_string):
#     return echo_string.upper()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=default_port)
