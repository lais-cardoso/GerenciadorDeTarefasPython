from gerenciador.tarefas import *


def menu():
    print("\n=== GERENCIADOR DE TAREFAS - TURMA TESTES E MANUTENCAO DE SOFTWARE ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Buscar tarefa por número")
    print("6. Total de tarefas")
    print("7. Sair")

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
            titulo = input("Digite o título da tarefa: ")
            indice = buscar_tarefa(titulo)
            if indice != -1:
                print(f"Tarefa encontrada: {tarefas[indice]}")
            else:
                print("Tarefa não encontrada.")
        elif opcao == "5":
            indice = int(input("Número da tarefa: ")) 
            remover_tarefa(indice)
        
        elif opcao == "6":
            listar_tarefas_duplicada()

        

        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

executar()