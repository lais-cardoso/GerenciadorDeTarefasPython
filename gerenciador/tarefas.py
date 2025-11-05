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
    print(total_tarefas_concluidas())

def concluir_tarefa(indice):
    if indice >= 0 or indice < len(tarefas):
        tarefas[indice]["status"] = True  
        print("Tarefa concluída!")
        return
    print("Erro ao concluir tarefa.")

def remover_tarefa(indice):
    if indice >= 0 and indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida.")
        return
    print("Erro: índice inválido.")

def buscar_tarefa(titulo):
    for i, t in enumerate(tarefas):
        if t["titulo"] == titulo:
            return i
    return -1

def total_tarefas_concluidas():
    soma = 0
    for t in tarefas:
        if t["status"] == True:
            soma += 1
    return f"Total de tarefas concluídas: {soma}"
        

def listar_tarefas_duplicada():
    for t in tarefas:
        print(t["titulo"])


