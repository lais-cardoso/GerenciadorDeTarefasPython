from tarefas import *

def menu():
    print("\n=== GERENCIADOR DE TAREFAS - TURMA TESTES E MANUTENCAO DE SOFTWARE ===")
    print("1. Adicionar tarefas")
    print("2. Listar tarefas")
    print("3. Concluir tarefas")
    print("4. Remover tarefas")
    print("5. Buscar tarefas")
    print("6. Total de tarefas")
    print("7. Listar tarefas duplicadas")
    print("8. Sair")

def executar():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            adicionar_tarefa(titulo, descricao)
        elif opcao == "2":
            indice = int(input("Número da tarefa: ")) - 1
            listar_tarefas()
        elif opcao == "3":
            indice = int(input("Número da tarefa: ")) - 1
            concluir_tarefa(indice)
        elif opcao == "4":
            indice = int(input("Número da tarefa: ")) - 1
            remover_tarefa(indice)
        elif opcao == "5":
            indice = int(input("Número da tarefa: ")) - 1
            buscar_tarefa(indice)
        elif opcao == "6":
            indice = int(input("Número da tarefa: ")) - 1
            total_tarefas(indice)
        elif opcao == "7":
            indice = int(input("Número da tarefa: ")) - 1
            listar_tarefas_duplicada(indice)
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

executar()