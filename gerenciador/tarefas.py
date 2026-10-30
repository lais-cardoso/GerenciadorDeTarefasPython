tarefas = [ {"titulo": "Estudar Python", "descricao": "Preciso estudar para codar", "concluida": "não"}]

def adicionar_tarefa(titulo, descricao):
    tarefas.append({
        "titulo": titulo,
        "descricao": descricao,
        "concluida": "não"
    })
    print(f"Tarefa '{titulo}' adicionada!")  

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - Descrição: {t.get('descricao', 'Sem descrição')}")


def concluir_tarefa(indice):
    try:
        tarefas[indice-1]["concluida"] = "Sim"  
        print("Tarefa concluída!")
    except:
        print("Erro ao concluir tarefa.")

def remover_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Erro: número de tarefa inválido.")
        return

    tarefas.pop(indice - 1)
    print("Tarefa removida.")

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