from flask import Flask, render_template, request
from auth import register_user, login_user

app = Flask(__name__)


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login_page():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = login_user(username, password)

        if user:
            if user:
             return render_template(
             "dashboard.html",
             username=user
    )

        else:
            return "❌ Invalid username or password."

    return render_template("login.html")


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register_page():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        result = register_user(username, password)

        if result:
            return "✅ Account created successfully! <br><a href='/login'>Login now</a>"

        else:
            return "❌ Username already exists."


    return render_template("register.html")



# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(debug=True)