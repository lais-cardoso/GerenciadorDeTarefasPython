from gerenciador import tarefas

def gerar_relatorio():
    print("==== RELATÓRIO ====")
    print(f"Total de tarefas: {len(tarefas)}")
    print(f"Tarefas concluídas: {sum(1 for t in tarefas if t.get('concluida') == True)}")
    print(f"Tarefas pendentes: {sum(1 for t in tarefas if t.get('concluida') == False)}")