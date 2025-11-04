tarefas = []

def adicionar_tarefa(titulo, descricao):
    tarefa = {
        'titulo': titulo,
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada!")


def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")  

def concluir_tarefa(indice):
    try:
        tarefas[indice]["concluida"] = "Sim"  
        print("Tarefa concluída!")
    else:
        print("Erro: índice inválido.")


def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print(f"Tarefa '{indice}' removida.")
    else:
        print("Erro: índice inválido.")


def buscar_tarefa(titulo):
    for i, t in enumerate(tarefas):
        if t["titulo"].lower() == titulo.lower():
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
