tarefas = []

def adicionar_tarefa(titulo, descricao):
 
  if titulo is None or not str(titulo).strip():
    print("Erro: o campo 'titulo' é obrigatório.")
    return False
  if descricao is None or not str(descricao).strip():
    print("Erro: o campo 'descricao' é obrigatório.")
    return False
 
  nova_tarefa = {
  "titulo": titulo,
  "descricao": descricao,
  "concluida": False
  }
  
  tarefas.append(nova_tarefa)
  print(f"Tarefa '{titulo}' adicionada!") 

def listar_tarefas():
  if len(tarefas) == 0:
    print("Nenhuma tarefa cadastrada.")
  for i, t in enumerate(tarefas):
    print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")

def concluir_tarefa(indice):
  try:
    tarefas[indice - 1]["concluida"] = "Concluída" 
    print("Tarefa concluída!")
  except:
    print("Erro ao concluir tarefa.")

def remover_tarefa(indice):
  try:
    tarefas.pop(indice - 1)
    print("Tarefa removida.")
  except:
    print("Erro: índice inválido.")

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
