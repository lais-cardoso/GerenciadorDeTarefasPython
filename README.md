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

### Histórico de manutenção

1. **Corretiva:** A função `adicionar_tarefa` em `tarefas.py` não salva a tarefa na lista, apenas imprime uma mensagem no terminal. Com isso, nenhuma tarefa criada fica guardada no sistema.
2. **Corretiva:** Ao concluir uma tarefa em `tarefas.py`, o campo `concluida` é salvo com o texto `"Sim"` em vez do booleano `True`. Isso quebra o relatório em `relatorios.py` (que busca por `True`) e também causa erro na função `total_tarefas`.
3. **Corretiva:** O menu em `main.py` passa o número digitado pelo usuário direto para as funções de concluir e remover em `tarefas.py` sem subtrair 1. Como a listagem começa do índice 1 e as listas em Python começam do 0, o sistema tenta alterar ou remover a tarefa errada (ou dá erro de índice).
4. **Preventiva:** A função `listar_tarefas` em `tarefas.py` está com o laço de repetição duplicado (imprime a lista de tarefas duas vezes seguidas no terminal) e não interrompe quando a lista está vazia, poluindo o código e a tela.
5. **Preventiva:** No menu principal (`main.py`), a leitura do número da tarefa usa `int(input(...))` sem tratamento com `try/except`. Se o usuário digitar uma letra ou deixar em branco, o programa quebra com erro `ValueError`.

## Como executar
```bash
python main.py