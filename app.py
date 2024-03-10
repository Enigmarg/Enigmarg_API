from flask import Flask, jsonify, request
app = Flask(__name__)

# Listas do Usuários
usuarios = [
    {
      'id': 1,
      'usuário' : 'Guilherme'
    },    
    {
      'id': 2,
      'usuário' : 'Rafael'
    },    
    {
      'id': 3,
      'usuário': 'Gustavo'
    }
]


# Métodos da API
# Criação de Usuário utilizando o método POST
@app.route('/usuarios', methods =['POST'])
def adicionar_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)

    return jsonify(usuarios)

# Consultar todos os usuário GET
@app.route('/usuarios', methods= ['GET'])
def obter_usuario():

  return jsonify(usuarios)

# Consultar um usuário GET
@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_por_id(id):
  for usuario in usuarios:
      if usuario.get('id')== id:

        return jsonify(usuario)

# Modificar um usuário PUT  
@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario(id):
   usuario_alterado = request.get_json()
   for indice,usuario in enumerate(usuarios):
      if usuario.get('id')==id:
         usuarios[indice].update(usuario_alterado)
         
         return jsonify(usuarios[indice])

# excluir usuário DELETE
@app.route('/usuarios/<int:id>',methods=['DELETE'])
def excluir_usuario(id):
    for indice, usuario in enumerate(usuarios):
       if usuario.get('id')==id:
          del usuarios[indice]

          return jsonify(usuarios[indice])
print("Conexão bem-Sucessida")       

# Endpoint
app.run(port=6001,host='localhost',debug=True)