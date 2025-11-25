from gerenciador import tarefas, relatorios

usuarios = []

def cadastrar_usuario(nome, senha):
    for u in usuarios:
        if nome == u["nome"]:
            print("Esse nome de usuário já existe.")
            return
    if nome == "" or senha == "":
        print("Nome de usuário e senha não podem ser vazios.")
        return
    
    usuarios.append({"nome": nome, "senha": senha, "tarefas": []})
    print("Usuário cadastrado!")


def autenticar(nome, senha):
    
    
    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            tarefas.user_atual = usuario
            relatorios.user_atual = usuario

            print("Login bem-sucedido!")
            return True
    
    print("Usuário ou senha incorretos.")
    return False

def listar_usuarios():
    print("Usuários cadastrados:")
    for u in usuarios:
        print("-", u["nome"])