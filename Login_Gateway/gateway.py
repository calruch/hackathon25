import os
from flask import Flask, render_template, request, session, redirect, url_for, abort
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__, template_folder="templates")
app.secret_key = "You_Shall_Not_Pass"

service_passphrases = {
    "to-upper": "Huey",
    "who-is": "Dewey",
    "weather": "Louie",
}

service_ports = {
  "to-upper": 30081,
  "weather": 30082,
  "who-is": 30083,
}

# def create_credentials():
#     password = werkzeug.security.generate_password_hash("password123", method='scrypt', salt_length=16)
#     if not os.path.exists("credentials.txt"):
#         with open("credentials.txt", "w") as f:
#             f.write("admin:" + password + "\n")
#             f.write("user:" + password + "\n")

credentials = {}
with open("credentials.txt") as f:
    for line in f:
        if line.strip():
            user, pwd_hash = line.strip().split(":", 1)
            credentials[user] = pwd_hash

pathway_table = {}

@app.route("/", methods=["GET"])
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if check_password_hash(credentials.get(username, ""), password):
            session["logged_in"] = True
            session["secret_key"] = "Gandolf_the_White"
            return render_template("base.html")
        else:
            return render_template("login.html", error="Invalid credentials"), 401
    return render_template("login.html", error=None)

@app.route("/pathway", methods=["POST"])
def pathway():
    svc = request.form["service"]
    passphrase = request.headers.get("passphrase","")
    if service_passphrases.get(svc) != passphrase:
        abort(403)
    port = service_ports.get(svc)
    if port is None:
        abort(404)
    pathway_table[svc] = port
    return "OK", 200

@app.route("/<svc>/<user_key>")
def proxy(svc, user_key):
    if not session.get("logged_in"): return redirect(url_for("login"))
    if user_key != session["secret_key"]: abort(403)
    port = pathway_table.get(svc)
    if not port: abort(404)
    return redirect(f"http://localhost:{port}/{svc}/{user_key}")

if __name__ == "__main__":
    # create_credentials()
    app.run(host="0.0.0.0", port=5000)
