# api.py - Simulated API service
import threading
import time

from flask import Flask, jsonify

app = Flask(__name__)


def start_api():
    """Simulates starting a REST API."""

    def run():
        print("Starting API service...")
        time.sleep(1)
        app.run(port=5000)

    thread = threading.Thread(target=run)
    thread.start()


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "API is running"}), 200
