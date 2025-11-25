user_atual = None

def adicionar_tarefa(titulo, descricao):
    tarefa_OBJ = {
        "titulo": titulo,
        "descricao": descricao,
        "status": False
    }
    
    if user_atual == None:
        print("Usuário não encontrado! ", user_atual)
        return
    
    user_atual["tarefas"].append(tarefa_OBJ)
    print(f"Tarefa '{titulo}' adicionada!")

def listar_tarefas():
    if len(user_atual["tarefas"]) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
        
    for i, tarefas in enumerate(user_atual["tarefas"]):
        print(f"{i+1}. {tarefas['titulo']} - {'Concluida' if tarefas['status'] == True else 'Pendente'}\nDescrição: {tarefas['descricao']}\n")

    print(total_tarefas_concluidas())

def concluir_tarefa(indice):
    if 0 <= indice < len(user_atual["tarefas"]):
            user_atual["tarefas"][indice]["status"] = True  
            print("Tarefa concluída!")
            return
        
    print("Essa tarefa não existe.")

def remover_tarefa(indice):
    if 0 <= indice < len(user_atual["tarefas"]):
        user_atual["tarefas"].pop(indice)
        print("Tarefa removida.")
        return
    
    print("Essa tarefa não existe.")

def buscar_tarefa(termo):
    termo = termo.lower().strip() 

    resultados = []
    for t in user_atual["tarefas"]:
        if termo in t["titulo"].lower():
            resultados.append(t)

    if len(resultados) == 0:
        print("Nenhuma tarefa encontrada com esse termo.")
        return

    print(f"{len(resultados)} tarefa(s) encontrada(s):\n")
    for t in resultados:
        print(f"Título: {t['titulo']}")
        print(f"Descrição: {t['descricao']}")
        print(f"Status: {'Concluída' if t['status'] else 'Pendente'}\n")

def total_tarefas_concluidas():
    soma = sum(1 for tarefas in user_atual["tarefas"] if tarefas["status"] == True)
    return f"Total de tarefas concluídas: {soma}"
