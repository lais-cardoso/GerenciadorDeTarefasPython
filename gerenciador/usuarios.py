usuarios = []

def cadastrar_usuario(nome, senha):
    if nome is None or not str(nome).strip():
        print("Erro: Nome é obrigatório e não pode estar vazio!")
        return False
    if senha is None or not str(senha).strip():
        print("Erro: Senha é obrigatória e não pode estar vazia!")
        return False
    
    usuarios.append({"nome": nome, "senha": senha})
    print("Usuário cadastrado!")
    return True

def listar_usuarios():
    print("Usuários cadastrados:")
    for u in usuarios:
        print("-", u["nome"])