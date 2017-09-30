import os
from flask import Flask

PORT = int(os.getenv("PORT", "5000"))

app = Flask("lifeinteal-bot")


@app.route('/')
def home():
    return "ohai"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT, threaded=True)
