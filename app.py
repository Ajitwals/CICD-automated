from flask import Flask, jsonify

app = Flask(__name__)

# Mock user data
users = {
    1: {"id": 1, "name": "Ajit"},
    2: {"id": 2, "name": "pratya"},
    3: {"id": 3, "name": "wals"}
}

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
