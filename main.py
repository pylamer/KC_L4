import flask
import time
import random
from utils import get_secret_number

URL_SEC_NUMBER = 'https://lab.karpov.courses/hardml-api/module-5/get_secret_number'

app = flask.Flask(__name__)


@app.route("/return_secret_number")
def hello():
    time.sleep(1)
    print("get started")
    return flask.jsonify(secret_number=secret_number, random_number=random.randint(1, 10))


if __name__ == "__main__":
    secret_number = get_secret_number(URL_SEC_NUMBER)
    print(secret_number)
    app.run()
else:
    application = app

