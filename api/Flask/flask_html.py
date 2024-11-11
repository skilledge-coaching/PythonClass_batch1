#render_template

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("python.html") #, content = name, r = 45

if __name__ == "__main__":
    app.run(debug= True)