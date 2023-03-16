from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")
