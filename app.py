import os
import logging
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
    log.debug("Form: " + str(request.form))
    return request.form.get("challenge") or "wat"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT, threaded=True)
