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
        status = 'Concluída' if t['concluida'] else 'Pendente'
        print(f"{i+1}. {t['titulo']} - {status}")


def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
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
    return sum(t["concluida"] for t in tarefas)


def listar_tarefas_duplicada():
    for t in tarefas:
        print(t["titulo"])
