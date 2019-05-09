from flask import Flask, jsonify
import yaml

app = Flask(__name__, static_url_path='')


@app.route("/server")
def serve_yml():
    with open('./file.yml', 'r') as out:
        cfg = yaml.load(out)
    return jsonify(cfg)