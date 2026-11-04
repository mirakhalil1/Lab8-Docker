from flask import Flask, jsonify
from database import get_users, create_db_table

app = Flask(__name__)

@app.route("/get_users", methods=["GET"])
def users_names():
    users = get_users()
    return jsonify([user["name"] for user in users])

if __name__ == "__main__":
    create_db_table()
    app.run(host="0.0.0.0", port=3000)
