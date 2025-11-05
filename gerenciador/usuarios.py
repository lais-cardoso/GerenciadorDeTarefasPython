usuarios = []

def cadastrar_usuario(nome, senha):
    if not nome or not senha:
        print("Erro: Nome e senha não podem estar vazios!")
        return
     
    usuarios.append({"nome": nome, "senha": senha})
    print("Usuário cadastrado!")

def autenticar(nome, senha):
    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print("Login bem-sucedido!")
            return True
    print("Usuário ou senha incorretos.")
    return False

def listar_usuarios():
    print("Usuários cadastrados:")
    for u in usuarios:
        print("-", u["nome"])