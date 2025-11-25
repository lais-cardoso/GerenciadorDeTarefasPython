
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
    indice_real = indice - 1
    try:
        if 0 <= indice_real < len(tarefas):
            tarefas[indice_real]["concluida"] = True
            print(f"Tarefa '{tarefas[indice_real]['titulo']}' concluída!")
        else:
            raise IndexError 
    except IndexError:
        print("Erro: índice inválido. O número da tarefa deve ser maior que zero e estar na lista.")
    except TypeError:
        print("Erro: a entrada deve ser um número inteiro.")
def remover_tarefa(indice):
    indice_real = indice - 1
    try:
        tarefas.pop(indice_real)
        print("Tarefa removida.")
    except IndexError:
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
def listar_tarefas_duplicadas():
    contagem_titulos = {}
    for t in tarefas:
        titulo = t["titulo"]
        contagem_titulos[titulo] = contagem_titulos.get(titulo, 0) + 1

    duplicatas = []
    
    for titulo, count in contagem_titulos.items():
        if count > 1:
            duplicatas.append(titulo)

    if duplicatas:
        print("Títulos de tarefas duplicadas:")
        for d in duplicatas:
            print(f"- {d}")
    else:
        print("Nenhuma tarefa duplicada encontrada.")

def editar_tarefa(indice, novo_titulo=None, nova_descricao=None):
    indice_real = indice - 1
    try:
        tarefa = tarefas[indice_real]

        if novo_titulo and novo_titulo.strip():
            tarefa["titulo"] = novo_titulo

        if nova_descricao and nova_descricao.strip():
            tarefa["descricao"] = nova_descricao

        print(f"Tarefa {indice} editada com sucesso!")
    
    except IndexError:
        print("Erro: índice inválido para edição.")
