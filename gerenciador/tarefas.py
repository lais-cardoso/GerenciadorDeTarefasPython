
tarefas = []

def adicionar_tarefa(titulo, descricao, concluida=False):

   
    if titulo is None or not str(titulo).strip():
        print("Erro: o campo 'titulo' é obrigatório.")
        return False
    if descricao is None or not str(descricao).strip():
        print("Erro: o campo 'descricao' é obrigatório.")
        return False

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "concluida": concluida
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada!")
    return True

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")
def listar_tarefas_completas():
    for i, t in enumerate(tarefas):
        if t["concluida"]:
            print(f"{i+1}. {t['titulo']} - Concluída") 

def concluir_tarefa(indice):
    try:
        tarefas[indice]["concluida"] = True
        print("Tarefa concluída.")
    except:
        print("Erro: índice inválido.")

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

def total_tarefas():
    soma = 0
    for t in tarefas:
        soma += t["concluida"]  
    return soma

def listar_tarefas_duplicada():
    titulos = {}
    for t in tarefas:
        print(t["titulo"])
