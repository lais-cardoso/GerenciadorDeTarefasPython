tarefas = []

def adicionar_tarefa(titulo, descricao):
    if not titulo or not descricao:
        print("Erro: Título e descrição não podem estar vazios!")
        return
        
    tarefa = {"titulo": titulo, "descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")
    
def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")

def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")  

def concluir_tarefa(indice):
    # Ajusta o índice pois a lista mostrada começa em 1
    indice = indice - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa concluída!")
    else:
        print("Erro: índice inválido.")
   
def remover_tarefa(indice):
    # Ajusta o índice pois a lista mostrada começa em 1 
    indice = indice - 1
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida.")
    else:
        print("Erro: índice inválido.")
        
def buscar_tarefa(titulo):
    for i, t in enumerate(tarefas):
        if t["titulo"] == titulo:
            return i
    return -1

def total_tarefas():
    soma = 0
    for t in tarefas:
        if t["concluida"]:
            soma += 1
    return soma
    soma += t["concluida"]  
    return soma