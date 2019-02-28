from flask import Flask
from flask import jsonify
import logging
import time
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO)

START_TIME = time.time()

app = Flask(__name__)

def _load_json_files_into_dict(filename):

    json_payload = None

    try:
        with open(filename) as file_obj:
            json_payload = json.load(file_obj)
            logging.info("Loaded filename successfully: " + filename)
    except Exception as e:
        logging.info("Unable to load filename: " + filename)
        logging.info(e)

    return json_payload

BUILD_METADATA = _load_json_files_into_dict("build_metadata.json")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/healthcheck")
def healthcheck():

    time_now = time.time()

    hc_payload = {
        "myapplication": [
            {
                "version": BUILD_METADATA["version"],
                "description" : "pre-interview technical test",
                "lastcommitsha": BUILD_METADATA["lastcommitsha"],
                "uptime": time_now - START_TIME
            }
        ]
    }
    return jsonify(hc_payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
