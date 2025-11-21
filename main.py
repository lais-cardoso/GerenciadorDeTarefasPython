from gerenciador import tarefas, usuarios, relatorios

def login_ou_cadastro():
    while True:
        print("\n====== LOGIN / CADASTRO ======")
        print("1. Login")
        print("2. Cadastro")
        print("0. Sair")

        opcao = input("Escolha: ")

        match opcao:

            case "1":
                nome = input("Usuário: ")
                senha = input("Senha: ")
                
                if usuarios.autenticar(nome, senha):
                    menu()
            
            case "2":
                nome = input("Nome de usuário: ")
                senha = input("Senha: ")
                usuarios.cadastrar_usuario(nome, senha)

            case "0":
                print("Saindo...")
                break
            
            case _:
                print("Opção inválida")

def menu():
    
    while True:
        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Buscar tarefa")
        print("4. Concluir tarefa")
        print("5. Remover tarefa")
        print("6. Relatório")
        print("7. Listar usuários")
        print("0. Sair")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                tarefas.adicionar_tarefa(titulo, descricao)

            case "2":
                tarefas.listar_tarefas()

            case "3":
                titulo = input("Título: ")
                tarefas.buscar_tarefa(titulo)

            case "4":
                try:
                    indice = int(input("Número da tarefa: "))
                    tarefas.concluir_tarefa(indice-1)
                except ValueError:
                    print("Digite um valor válido.")

            case "5":
                try:
                    indice = int(input("Número da tarefa: "))
                    tarefas.remover_tarefa(indice-1)
                except ValueError:
                    print("Digite um valor válido.")

            case "6":
                relatorios.gerar_relatorio()

            case "7":
                usuarios.listar_usuarios()

            case "0":
                print("Saindo...")
                break

            case _:
                print("Opção inválida.")

login_ou_cadastro()