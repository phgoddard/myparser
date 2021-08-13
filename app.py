from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

from app.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

services = Services()


@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()

@app.route("/study", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def study():
    data = request.get_json()
    app.logger.info(f"/study - Got request: {data}")
    forms = services.get_study(data.get('studyname'),data.get('studyid'))
    app.logger.info(f"/study - Output: {forms}")
    return jsonify(forms)

@app.route("/file", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def file():
    data = request.get_json()
    app.logger.info(f"/file - Got request: {data}")
    forms = services.get_file()
    app.logger.info(f"/get_study - Output: {forms}")
    return jsonify(forms)

@app.route("/dialog", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def dialog():
    data = request.get_json()
    app.logger.info(f"/dialog - Got request: {data}")
    forms = services.get_dialog(data.get('filedata'))
    app.logger.info(f"/dialog - Output: {forms}")
    return jsonify(forms)


if __name__ == "__main__":
    app.run(host='0.0.0.0')