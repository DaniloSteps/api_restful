## Como executar a API

Tendo o Python3 e Python3-pip instalado, com seu terminal dentro da pasta api onde se localiza o codigo execute os seguintes comandos:

```
pip install -r requirements.txt
python3 app.py
```

## Rotas de usuários: 

Listar usuários:
curl -X GET http://127.0.0.1:5000/usuarios

Criar usuário:
curl -X POST http://127.0.0.1:5000/usuarios -H "Content-Type: application/json" -d '{"nome": "Maria Joana", "email": "maria_j00@exemplo.com"}'

Consultar usuário especifico:
curl -X GET http://127.0.0.1:5000/usuarios/1

Alterar dados de usuário:
curl -X PUT http://127.0.0.1:5000/usuarios/1 -H "Content-Type: application/json" -d '{"nome": "Maria Joana", "email": "maria.joana@exemplo.com"}'

Alterar dado parcial de usuário:
curl -X PATCH http://127.0.0.1:5000/usuarios/1 -H "Content-Type: application/json" -d '{"email":"maria_00@exemplo.com"}'

Deletar usuário:
curl -X DELETE http://127.0.0.1:5000/usuarios/1


## Rotas de publicações:

Criar um post:
curl -X POST http://127.0.0.1:5000/postagens -H "Content-Type: application/json" -d '{"titulo": "Primeiro post", "conteudo": "Ola mundo", "usuario_id": 1}'

Consultar post:
curl -X GET http://127.0.0.1:5000/postagens/1

Deletar post:
curl -X DELETE http://127.0.0.1:5000/postagens/1
