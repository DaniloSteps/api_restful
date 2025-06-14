from flask import Flask, jsonify, request
from database import db
from models import Usuario, Postagem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# --- Endpoints para Usuário ---

@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    """Retorna todos os usuários."""
    usuarios = Usuario.query.all()
    # Converte a lista de objetos Usuario para uma lista de dicionários JSON
    return jsonify([{'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email} for usuario in usuarios])

@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    """Retorna um usuário específico pelo ID."""
    usuario = Usuario.query.get_or_404(id)
    return jsonify({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email})

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    """Cria um novo usuário."""
    dados = request.json
    novo_usuario = Usuario(nome=dados['nome'], email=dados['email'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'id': novo_usuario.id}), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    """Atualiza completamente um usuário existente."""
    dados = request.json
    usuario = Usuario.query.get_or_404(id)
    usuario.nome = dados['nome']
    usuario.email = dados['email']
    db.session.commit()
    return jsonify({'id': usuario.id})

@app.route('/usuarios/<int:id>', methods=['PATCH'])
def atualizar_parcialmente_usuario(id):
    """Atualiza parcialmente um usuário existente."""
    dados = request.json
    usuario = Usuario.query.get_or_404(id)
    if 'nome' in dados:
        usuario.nome = dados['nome']
    if 'email' in dados:
        usuario.email = dados['email']
    db.session.commit()
    return jsonify({'id': usuario.id})

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    """Deleta um usuário."""
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'resultado': True})

# --- Endpoints para Postagem ---

@app.route('/postagens', methods=['GET'])
def obter_postagens():
    """Retorna todas as postagens."""
    postagens = Postagem.query.all()
    # Converte a lista de objetos Postagem para uma lista de dicionários JSON
    return jsonify([{'id': postagem.id, 'titulo': postagem.titulo, 'conteudo': postagem.conteudo, 'usuario_id': postagem.usuario_id} for postagem in postagens])

@app.route('/postagens/<int:id>', methods=['GET'])
def obter_postagem(id):
    """Retorna uma postagem específica pelo ID."""
    postagem = Postagem.query.get_or_404(id)
    return jsonify({'id': postagem.id, 'titulo': postagem.titulo, 'conteudo': postagem.conteudo, 'usuario_id': postagem.usuario_id})

@app.route('/postagens', methods=['POST'])
def criar_postagem():
    """Cria uma nova postagem."""
    dados = request.json
    # Assume que a classe do modelo foi renomeada para Postagem
    nova_postagem = Postagem(titulo=dados['titulo'], conteudo=dados['conteudo'], usuario_id=dados['usuario_id'])
    db.session.add(nova_postagem)
    db.session.commit()
    return jsonify({'id': nova_postagem.id}), 201

@app.route('/postagens/<int:id>', methods=['PUT'])
def atualizar_postagem(id):
    """Atualiza completamente uma postagem existente."""
    dados = request.json
    postagem = Postagem.query.get_or_404(id)
    postagem.titulo = dados['titulo']
    postagem.conteudo = dados['conteudo']
    db.session.commit()
    return jsonify({'id': postagem.id})

@app.route('/postagens/<int:id>', methods=['PATCH'])
def atualizar_parcialmente_postagem(id):
    """Atualiza parcialmente uma postagem existente."""
    dados = request.json
    postagem = Postagem.query.get_or_404(id)
    if 'titulo' in dados:
        postagem.titulo = dados['titulo']
    if 'conteudo' in dados:
        postagem.conteudo = dados['conteudo']
    db.session.commit()
    return jsonify({'id': postagem.id})

@app.route('/postagens/<int:id>', methods=['DELETE'])
def deletar_postagem(id):
    """Deleta uma postagem."""
    postagem = Postagem.query.get_or_404(id)
    db.session.delete(postagem)
    db.session.commit()
    return jsonify({'resultado': True})

if __name__ == '__main__':
    app.run(debug=True)
