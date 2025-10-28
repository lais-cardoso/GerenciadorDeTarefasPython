tarefas = []

def adicionar_tarefa(titulo, descricao):
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False
    }
    tarefas.append(tarefa)

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")

def concluir_tarefa(indice):
    try:
        tarefas[indice]["concluida"] = True
        print("Tarefa concluída!")
    except:
        print("Erro ao concluir tarefa.")

def remover_tarefa(indice):
    try:
        tarefas.pop(indice)
        print("Tarefa removida.")
    except:
        print("Erro: índice inválido.")