"""
Simple python flask app for the anz assessment

"""
import logging
import time
import json
from flask import Flask
from flask import jsonify

logging.basicConfig(level=logging.INFO)

START_TIME = time.time()

APP = Flask(__name__)

def _load_json_files_into_dict(filename):
    """
    dummy
    :param filename:
    :return:
    """
    json_payload = None

    try:
        with open(filename) as file_obj:
            json_payload = json.load(file_obj)
            logging.info("Loaded filename successfully")
    except IOError:
        logging.info("Unable to load file")

    return json_payload

BUILD_METADATA = _load_json_files_into_dict("build_metadata.json")

@APP.route("/")
def hello():
    """
    base endpoint
    :return:
    """
    return "Hello World!"

def prepare_health_check_payload():
    """
    Prepare the healt check payload outside of flask
    context so it's actually callable in test
    :return:
    """
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

    return hc_payload

@APP.route("/healthcheck")
def healthcheck():
    """
    endpoint for the assessment
    :return:
    """
    return jsonify(prepare_health_check_payload())

if __name__ == "__main__":
    APP.run(host="0.0.0.0")
