from flask import Flask,jsonify,request

app = Flask(__name__)

livros = [
    {
        'id' : 1,
        'titulo' : 'Senhor dos aneis',
        'autor' : 'J.R.R Tolkien',
    },
    {

        'id': 2,
        'titulo': 'Harry Potter',
        'autor': 'J.K.Howling',
    },
    {

        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Habitos atomicos',
    },
]

#Consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():  # put application's code here
    return jsonify(livros)



#Consulatar por (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)



# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate (livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])



#Incluir
@app.route('/livros/<int:id>', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(novo_livro)


#Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice,livro  in enumerate (livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
