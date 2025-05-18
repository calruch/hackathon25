import os
import requests
from flask import Flask, request, render_template, abort
from config import Config

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

@app.route("/weather/<secret_key>", methods=["GET", "POST"])
def main_page(secret_key):
    if secret_key != app.config["SECRET_KEY"]:
        abort(403)
    weather_info = None
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            city_query = city.replace(" ", "+")
            fmt = app.config.get("WEATHER_FORMAT", "3")
            resp = requests.get(f"http://wttr.in/{city_query}?format={fmt}")
            weather_info = resp.text
    return render_template("service.html", key=secret_key, weather=weather_info)

if __name__ == "__main__":
    port = int(os.getenv("PORT", app.config.get("PORT", 5001)))
    app.run(host="0.0.0.0", port=port)