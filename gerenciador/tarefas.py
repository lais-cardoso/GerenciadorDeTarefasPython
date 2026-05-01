tarefas = []


def adicionar_tarefa(titulo, descricao):
    tarefas.append({"titulo": titulo, "descricao": descricao})
    print(f"Tarefa '{titulo}' adicionada!")


def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, t in enumerate(tarefas):
        print(
            f"{i + 1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}"
        )


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


def buscar_tarefa(titulo):
    for i, t in enumerate(tarefas):
        if t["titulo"] == titulo:
            return i
    return -1


def total_tarefas_concluidas():
    return sum(1 for t in tarefas if t.get("concluida"))
