from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("01 index.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/user_input")
def user_input():
    return render_template("02 dropdown.html")

@app.route("/suggestions")
def suggestions():
    return render_template("03 map.html")

if __name__ == "__main__":
    app.run(debug=True)