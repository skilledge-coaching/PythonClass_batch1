from flask import Flask

app = Flask(__name__)

@app.route("/helo_world")
def hello_world():
    return "<h1>Hello World<h1>"

@app.route("/user")
def user():
    return "this is user page"


if __name__ == "__main__":
    app.run(debug=True)