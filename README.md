# Gerenciador de Tarefas Python

Este projeto é um sistema simples de gerenciamento de tarefas.

## Estrutura
- `tarefas.py`: controla tarefas
- `usuarios.py`: controla usuários
- `relatorios.py`: gera relatórios
- `main.py`: menu principal

### Tipos de manutenção a aplicar:
- Corretiva: corrigir erros no código
- Evolutiva: adicionar funcionalidades novas
- Preventiva: melhorar código e documentação
- Adaptativa: ajustar compatibilidade e padrões

### Histórico de manutenção Grupo1[Leonardo Oliveira e Robert]

# Arquivo : tarefas.java

-Erro de output duplicado que estava presente na linha 18 [corrigido-Leonardo]

-Erro ao criar uma tarefa titulo e descrição não estão como obrigatorio[corrigido-Leonardo]

-Erro ao concluir tarefa a tarefa não estava sendo concluida ao colocar o indice[corrigido-Leonardo]

-A função de lista duplicada não estava cumprindo a sua função de encontrar tarefas duplicadas[corrigido-Leonardo]

# ARQUIVO: relatório.java
-Erro não tem lista de tarefas completas e não estava mostrando as tarefas conluidas no relatorio[corrigido-Leonardo]


# ARQUIVO: usario.java
-Erro ao criar um usuario o nome e senha não estão como obrigatorio[corrigido-Leonardo]



## MELHORIAS IMPLEMENTADAS:




## Como executar
```bash
python main.py

## Erros encontrados no código
- Depois de realizar a função de Adicionar tarefa ao tentar Listar Tarefas ele fala que nenhuma tarefa esta cadastrada - Corretiva
- As palavras estao escritas como "tarefa" ao inves de "tarefas" nas funções 1, 3, 4, 5. - Corretiva
- Ao tentar Concluir tarefa e Remover tarefa o codigo pede o Numero da tarefa mesmo que o numero não tenha sido pedido para ser definido em nenhum momento - Perfectiva
- As linhas 17,18 e 19,20 no tarefas.py estão duplicadas - Preventiva

- é possivel adicionar uma tarefa sem titulo e descrição
- é possivel adicionar um usuario sem nome e senha
- em relatorios esta escrito "from gerenciador.tarefas import tarefas" quando deveria estar "from gerenciador import tarefas"
- Ao tentar adicionar uma tarefa ela é duplicada
- Em tarefas.py na linha 24 o resultado está como "Sim" quando deveria estar em boolean: 
