from gerenciador.tarefas import tarefas

def gerar_relatorio():
  total = len(tarefas)
  concluidas = sum(1 for t in tarefas if t.get("concluida") == True)
  pendentes = total - concluidas

  print("==== RELATÓRIO ====")
  print(f"Total de tarefas: {total}")
  print(f"Tarefas concluídas: {concluidas}")
  print(f"Tarefas pendentes: {pendentes}")