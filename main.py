from tarefas import *

def menu():
    print("\n=== GERENCIADOR DE TAREFAS - TURMA TESTES E MANUTENCAO DE SOFTWARE ===")
    print("1. Adicionar tarefas")
    print("2. Listar tarefas")
    print("3. Concluir tarefas")
    print("4. Remover tarefas")
    print("5. Sair")

def executar():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            adicionar_tarefa(titulo, descricao)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            indice = int(input("Número da tarefa: ")) - 1
            concluir_tarefa(indice)
        elif opcao == "4":
            indice = int(input("Número da tarefa: ")) - 1
            remover_tarefa(indice)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

executar()