from tarefas import *

def menu():
    print("\n=== GERENCIADOR DE TAREFAS - TURMA TESTES E MANUTENCAO DE SOFTWARE ===")
    print("1. Adicionar tarefa")
    print("2. Buscar tarefa")
    print("3. Listar tarefas")
    print("4. Concluir tarefa")
    print("5. Remover tarefa")
    print("6. Sair")

def executar():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            adicionar_tarefa(titulo, descricao)
            
        elif opcao == "2":
            titulo = input("Título da tarefa a buscar: ")
            buscar_tarefa(titulo)
        elif opcao == "3":
            listar_tarefas()
        elif opcao == "4":
            indice = int(input("Número da tarefa: ")) - 1
            concluir_tarefa(indice)
        elif opcao == "5":
            indice = int(input("Número da tarefa: ")) - 1
            remover_tarefa(indice)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

executar()