import os
import logging
import json
from flask import Flask, request

PORT = int(os.getenv("PORT", "5000"))

app = Flask("lifeinteal-bot")

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def home():
    return "ohai"


@app.route('/', methods=['POST'])
def challenge():
    message = request.json
    log.debug("Message: " + json.dumps(message))
    if message and message.get("body") and message["body"].get("challenge"):
        return message["body"]["challenge"]
    return "wat"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT, threaded=True)
