# Gerenciador de Tarefas Python

Este projeto é um sistema simples de gerenciamento de tarefas.

## Estrutura
- `tarefas.py`: controla tarefas
- `usuarios.py`: controla usuários
- `relatorios.py`: gera relatórios
- `main.py`: menu principal


## Execução
```bash
python main.py
```

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