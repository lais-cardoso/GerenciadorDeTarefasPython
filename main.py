from gerenciador import tarefas, usuarios, relatorios

def menu():
    while True:
        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1. Adicionar tarefas")
        print("2. Listar tarefas")
        print("3. Concluir tarefas")
        print("4. Remover tarefas")
        print("5. Relatório")
        print("6. Usuários")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            tarefas.adicionar_tarefa(titulo, descricao)

        elif opcao == "2":
            tarefas.listar_tarefas()

        elif opcao == "3":
            indice = int(input("Número da tarefa: "))
            tarefas.concluir_tarefa(indice)

        elif opcao == "4":
            indice = int(input("Número da tarefa: "))
            tarefas.remover_tarefa(indice)

        elif opcao == "5":
            relatorios.gerar_relatorio()

        elif opcao == "6":
            nome = input("Nome: ")
            senha = input("Senha: ")
            
            if usuarios.cadastrar_usuario(nome, senha):
                usuarios.listar_usuarios()
            else:
                print("Cadastro não realizado devido a dados incompletos.")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()