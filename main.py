from gerenciador import tarefas, usuarios, relatorios


def menu():
    while True:
        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Relatório")
        print("6. Usuários")
        print("0. Sair")

        opcao = int(input("Escolha: "))

        match opcao:
            case "1":
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                tarefas.adicionar_tarefa(titulo, descricao)
            case "2":
                tarefas.listar_tarefas()
            case "3":
                indice = int(input("Número da tarefa: "))
                tarefas.concluir_tarefa(indice)
            case "4":
                indice = int(input("Número da tarefa: "))
                tarefas.remover_tarefa(indice)
            case "5":
                relatorios.gerar_relatorio()
            case "6":
                nome = input("Nome: ")
                senha = input("Senha: ")
                usuarios.cadastrar_usuario(nome, senha)
                usuarios.listar_usuarios()
            case "0":
                print("Saindo...")
                return
            case _:
                print("Opção inválida.")


menu()
