user_atual = None

def gerar_relatorio():
    total = len(user_atual["tarefas"])
    concluidas = sum(1 for t in user_atual["tarefas"] if t["status"] == True)
    pendentes = total - concluidas

    print(f"Total de tarefas: {total}")
    print(f"Tarefas concluídas: {concluidas}")
    print(f"Tarefas pendentes: {pendentes}")