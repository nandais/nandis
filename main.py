from flask import Flask, render_template

app = Flask(__name__)

# Lista de cursos (exemplo)
cursos = [
    {"nome": "Astronomia para curiosos", "descricao": "Entenda nosso incrível universo."},
    {"nome": "Empreendedor mirim", "descricao": "Aprenda a empreender de forma simples"},
    {"nome": "Criação de jogos", "descricao": "Crie jogos e aprenda a programar."}
]

@app.route("/")
def index():
    return render_template("index.html", cursos=cursos)

@app.route("/curso")
def curso():
    return render_template("curso.html")

@app.route("/contato")
def contato():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

