usuarios = []

def cadastrar_usuario(nome, senha):
    usuarios.append({"nome": nome, "senha": senha})
    print("Usuário cadastrado!")

    if nome is None or not str(nome).strip():
        print("Erro: o campo 'nome' é obrigatório.")
        return False
    if senha is None or not str(senha).strip():
        print("Erro: o campo 'senha' é obrigatório.")
        return False

def listar_usuarios():
    print("Usuários cadastrados:")
    for u in usuarios:
        print("-", u["nome"])