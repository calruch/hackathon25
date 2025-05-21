import random
import socket
import requests
from flask import Flask, jsonify, render_template, abort, url_for


set_port = 5000 # CHANGE THIS for port hopping


service = "pokequiz"
secret_key = "Gandolf_the_White" # Prevents access if not logged in via frontend gateway
ip = socket.gethostbyname(socket.gethostname())
app = Flask(__name__, template_folder="templates")

# PokeAPI stuff
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"
SPRITE_URL = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
    "sprites/pokemon/other/showdown/{}.gif"
)
TOTAL_POKEMON = 1025


def get_random_pokemon():
    poke_ids = random.sample(range(1, TOTAL_POKEMON + 1), 4)
    options = []
    for pid in poke_ids:
        resp = requests.get(f"{POKEAPI_URL}{pid}")
        if resp.ok:
            options.append(resp.json()["name"].capitalize())
        else:
            options.append(f"Unknown-{pid}")

    correct_index = random.randrange(len(options))
    correct_name = options[correct_index]
    sprite_url = SPRITE_URL.format(poke_ids[correct_index])

    return {
        "options": options,
        "correct_name": correct_name,
        "sprite_url": sprite_url
    }


@app.route(f"/{service}/<key>")
def quiz(key):
    if key != secret_key:
        abort(403)
    return render_template('pokequiz.html', key=key)


@app.route(f"/{service}/<key>/question")
def question(key):
    if key != secret_key:
        abort(403)
    return jsonify(get_random_pokemon())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=set_port)
