# API - É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Criar um api que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL base - localhost
# 3. Endpoints - 
    # - localhost/livros(GET)
    # - localhost/livros/id(POST)
    # - localhost/livros/id(GET)
    # - localhost/livros/id(PUT)
    # - localhost/livros/id(DELETE)
# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'o Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'A Guerra dos Tronos',
        'autor': 'George R.R. Martin'
    }
]

# Consultar(todo)
@app.route('/livros',methods=['GET']) # methods GET aceita que somente o metodo GET seja executado
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar

# Excluir

app.run(port=5000,host='localhost',debug=True)