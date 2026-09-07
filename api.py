from flask import Flask, jsonify, request

from app import get_user_by_id

app = Flask(__name__)


@app.route("/api/users")
def users():
    user_id = request.args.get("id")
    return jsonify(get_user_by_id(user_id))
