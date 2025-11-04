tarefas = []

def adicionar_tarefa(titulo, descricao):
    tarefa_OBJ = {
        "titulo": titulo,
        "descricao": descricao,
        "status": False
    }
    
    tarefas.append(tarefa_OBJ)
    
    print(f"Tarefa '{titulo}' adicionada!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'Concluida' if t['status'] == True else 'Pendente'}")

def concluir_tarefa(indice):
    try:
        tarefas[indice]["concluida"] = "Sim"
        print("Tarefa concluída!")
    except:
        print("Erro ao concluir tarefa.")

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


