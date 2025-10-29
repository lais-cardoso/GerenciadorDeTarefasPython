a = []
tarefas = []

def adicionar_tarefa(titulo, descricao):
    tarefas.append({"titulo": titulo, "descricao": descricao, "concluida": False})
    print(f"Tarefa '{titulo}' adicionada!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {'Concluída' if t['concluida'] else 'Pendente'}")
    

def concluir_tarefa(indice):
    try:
        tarefas[indice]["concluida"] = "Sim"
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

def total_tarefas():
    return len(tarefas)

def listar_tarefas_duplicada():
    titulos = {}
    for t in tarefas:
        if t["titulo"] in titulos:
            titulos[t["titulo"]] += 1
            print(f"Título Total: {t['titulo']} (Total: {titulos[t['titulo']]})")
        else:
            titulos[t["titulo"]] = 1
    for titulo, count in titulos.items():
        if count > 1:
            print(f"Título duplicado: {titulo} (Total: {count})")

