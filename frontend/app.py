import os
from flask import (
    Flask, render_template, request, session,
    redirect, url_for, abort
)
from werkzeug.security import check_password_hash

app = Flask(__name__, template_folder="templates")
app.config.from_object("config.Config")

app.jinja_env.globals["add-cat_url"] = app.config["ADD-CAT_URL"]
app.jinja_env.globals["weather_url"] = app.config["WEATHER_URL"]

credentials = {}
with open(app.config["CREDENTIALS_FILE"]) as f:
    for line in f:
        if line.strip():
            user, pwd_hash = line.strip().split(":", 1)
            credentials[user] = pwd_hash

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        stored = credentials.get(username, "")
        if check_password_hash(stored, password):
            session["logged_in"] = True
            session["username"] = username
            session["secret_key"] = app.config["SESSION_KEY"]
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials"), 401
    return render_template("login.html", error=None)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/add-cat")
def add_cat():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("add-cat.html")

@app.route("/weather")
def weather():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("weather.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
