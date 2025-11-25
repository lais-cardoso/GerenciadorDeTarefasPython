import os 
from gerenciador import tarefas, usuarios, relatorios

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def login_ou_cadastro():
    while True:
        print("\n====== LOGIN / CADASTRO ======")
        print("1. Login")
        print("2. Cadastro")
        print("0. Sair")

        opcao = input("Escolha: ")

        match opcao:

            case "1":
                nome = input("Usuário: ").strip()
                senha = input("Senha: ").strip()
                
                if nome == "" or senha == "":
                    print("Nome de usuário e senha não podem ser vazios.")
                    continue
                
                if usuarios.autenticar(nome, senha):
                    menu()
            
            case "2":
                nome = input("Nome de usuário: ").strip()
                senha = input("Senha: ").strip()
                usuarios.cadastrar_usuario(nome, senha)

            case "0":
                print("Saindo...")
                break
            
            case _:
                print("Opção inválida")

def menu():
    print("Bem-vindo", tarefas.user_atual["nome"], "!")
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
                limpar_terminal()
                print ("====== ADICIONAR TAREFA ======")
                titulo = input("Título: ").strip()
                descricao = input("Descrição: ").strip()
                
                if titulo == "" or descricao == "":
                    print("Título e descrição não podem ser vazios.")
                    continue
                
                tarefas.adicionar_tarefa(titulo, descricao)

            case "2":
                limpar_terminal()
                print ("====== LISTA DE TAREFAS ======")
                tarefas.listar_tarefas()

            case "3":
                limpar_terminal()
                print ("====== BUSCAR TAREFA ======")
                if len(tarefas.user_atual["tarefas"]) > 0:
                    while True:
                        termo = input("Digite o título (ENTER para voltar): ").strip()
                        
                        if termo == "":
                            break
                        
                        resultado = tarefas.buscar_tarefa(termo)
                        
                        if resultado is not None:
                            break
                else:
                    print("Nenhuma tarefa cadastrada.")
                    continue

            case "4":
                limpar_terminal()
                print("====== CONCLUIR TAREFAS ======")

                if len(tarefas.user_atual["tarefas"]) > 0:

                    tarefas.listar_tarefas()

                    while True:
                        valor = input("Número da tarefa (0 para voltar): ")

                        if valor == "0":
                            break  

                        if not valor.isdigit():
                            print("Digite um número válido.")
                            continue

                        indice = int(valor) - 1

                        if 0 <= indice < len(tarefas.user_atual["tarefas"]):
                            tarefas.concluir_tarefa(indice)
                            break
                        else:
                            print("Esse número não existe. Tente novamente.")

                else:
                    print("Nenhuma tarefa cadastrada.")
                    continue

            case "5":
                limpar_terminal()
                print("====== REMOVER TAREFAS ======")

                if len(tarefas.user_atual["tarefas"]) > 0:
                    
                    tarefas.listar_tarefas()

                    while True:
                        valor = input("Número da tarefa: (0 para voltar): ")

                        if valor == "0":
                            break
                        
                        if not valor.isdigit():
                            print("Digite um número válido.")
                            continue

                        indice = int(valor) - 1

                        if 0 <= indice < len(tarefas.user_atual["tarefas"]):
                            tarefas.remover_tarefa(indice)
                            break
                        else:
                            print("Esse número não existe. Tente novamente.")
                else:
                    print("Nenhuma tarefa cadastrada.")
                    continue

            case "6":
                limpar_terminal()
                print ("====== RELATÓRIO DE TAREFAS ======")
                relatorios.gerar_relatorio()

            case "7":
                limpar_terminal()
                print ("====== LISTA DE USUÁRIOS ======")
                usuarios.listar_usuarios()

            case "0":
                limpar_terminal()
                print("Saindo...")
                break

            case _:
                print("Opção inválida.")

login_ou_cadastro()