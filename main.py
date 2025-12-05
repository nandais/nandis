from flask import Flask, render_template
app = Flask(__name__)

# Lista de cursos (exemplo)
cursos = [
    { "id" : 1,
    "nome": "Astronomia para curiosos",
     "descricao": "Entenda nosso incrível universo."
     },
    { "id" : 2,
    "nome": "Empreendedor mirim",
     "descricao": "Aprenda a empreender de forma simples"
     },
    { "id" : 3,
    "nome": "Criação de jogos",
     "descricao": "Crie jogos e aprenda a programar."}
]

@app.route("/")
def index():
    return render_template("index.html", cursos=cursos)


@app.route("/contato")
def contato():
    return render_template("contact.html")

@app.route("/curso/<int:id>")
def curso(id):
    return render_template("curso.html", id = id)

    curso_selecionado = None
    
    for c in cursos:
        if c.get('id') == id:
            curso_selecionado = c
            break
    if curso_selecionado:
        return render_template("curso.html", curso=curso_selecionado)
    else:
        return "Curso não encontrado", 404


if __name__ == "__main__":
    app.run(debug=True)

