from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/home")
def welcome():
    return "Welcome to the Python Course"

@app.route("/admin")
def admin():
    return redirect(url_for("helo", name = "Arun"))

@app.route("/<name>")
def helo(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug = True)