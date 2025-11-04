a = []
b = "TituloPadrao"
c = 0
d = "DescPadrao"
e = True
f = None
g = "Hoje"

tarefas = [] # Lista global, correta!

def adicionar_tarefa(titulo, descricao):
    # 1. Cria o dicionário da nova tarefa
    nova_tarefa = {
        'titulo': titulo,
        'descricao': descricao, # Adiciona a descrição (opcional, mas bom ter)
        'concluida': False      # Status inicial sempre Pendente
    }
    print(titulo)
    print(descricao)
    
    # 2. Adiciona a tarefa à lista global 'tarefas'
    tarefas.append(nova_tarefa)

    print("aa")
    
    print(f"Tarefa '{titulo}' adicionada!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
        
    print("\n--- Lista de Tarefas ---")
    for i, t in enumerate(tarefas):
        # Usando 't.get' é uma prática mais segura caso o campo falte
        status = 'Concluída' if t.get('concluida') else 'Pendente'
        titulo = t.get('titulo', 'Tarefa sem título')
        print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")
        # for i, t in enumerate(tarefas):


def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
         tarefas[indice]["concluida"] = True
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'concluida' if t['concluida'] else 'pendente'} ")

def remover_tarefa(indice):
    try:
        tarefas.pop(indice)
        print("Tarefa removida.")
    except:
        print("Erro: índice inválido.")

def buscar_tarefa(titulo):
    for i, t in enumerate(tarefas):
        if t["titulo"] == titulo:
            return i
    return -1

def total_tarefas():
    soma = 0
    for t in tarefas:
        soma += t["concluida"]  
    return soma

def listar_tarefas_duplicada():
    for t in tarefas:
        print(t["titulo"])