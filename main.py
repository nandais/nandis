from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/curso")
def curso():
    return render_template("curso.html")

@app.route("/contato")
def contato():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
