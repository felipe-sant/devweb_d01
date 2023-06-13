from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask("__name__", static_folder="./static", template_folder="./template")

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'fatec'
app.config['MYSQL_PASSWORD'] = 'P@ssword1234'
app.config['MYSQL_DB'] = 'UNES'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quem_somos/")
def quem_somos():
    return render_template("quem_somos.html")

@app.route("/contato/", methods=['POST','GET'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES(%s, %s, %s)", (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return render_template("index.html");

    return render_template("contato.html")

@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("select * from contato")
    if users > 0:
        userDetails = cur.fetchall()
    return render_template("usuarios.html", userDetails = userDetails)
