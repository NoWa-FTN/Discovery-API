import requests  # Import pour les appels API
from flask import Flask, render_template, request, jsonify, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secretkey123"  # Clé secrète pour la gestion des sessions

# Utilisateurs fictifs pour la démonstration
users = {"admin": "password123", "user": "pass456"}


@app.route("/")
def home():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if username in users and users[username] == password:
            session["username"] = username
            return jsonify({"message": "Login successful", "redirect": "/"}), 200
        return jsonify({"message": "Invalid username or password"}), 401

    return render_template("login.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    return jsonify({"message": "Logged out successfully", "redirect": "/login"}), 200


@app.route("/api-posts", methods=["GET"])
def get_posts():
    """
    Récupère les 5 premiers articles fictifs d'une API externe.
    """
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()  # Vérifie si la requête est réussie
        posts = response.json()[:5]  # On récupère les 5 premiers articles
        return jsonify(posts), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch posts", "details": str(e)}), 500


if __name__ == "__main__":
    print("Starting Flask app on http://127.0.0.1:5000")
    app.run(debug=True)
