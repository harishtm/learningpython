from flask import Flask, abort

app = Flask(__name__)


@app.route("/")
def fake_gateway_timeout_error():
    abort(504)


if __name__ == "__main__":
    app.run(port=5000, debug=True)