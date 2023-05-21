import flask
import time

app = flask.Flask(__name__)


@app.route("/return_secret_number")
def hello():
    time.sleep(1)
    return "hello"


if __name__ == "__main__":
    app.run()
else:
    application = app

