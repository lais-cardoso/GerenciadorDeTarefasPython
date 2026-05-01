from gerenciador.tarefas import tarefas
from gerenciador.tarefas import total_tarefas_concluidas


def gerar_relatorio():
    total = len(tarefas)
    concluidas = total_tarefas_concluidas()
    pendentes = total - concluidas

    print("==== RELATÓRIO ====")
    print(f"Total de tarefas: {total}")
    print(f"Tarefas concluídas: {concluidas}")
    print(f"Tarefas pendentes: {pendentes}")
