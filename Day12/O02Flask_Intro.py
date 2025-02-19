
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2> Hello World <h2>"

@app.route("/<usrname>")
def user(usrname):
    return f"<h2> Greeting {usrname}, Welcome to FLASK....</h2>"

@app.route("/admin")
def admin():
    # return redirect(url_for("home"))
    return redirect(url_for("user", usrname="Mike Tyson" ))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
