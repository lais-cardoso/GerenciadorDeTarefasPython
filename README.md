# Gerenciador de Tarefas Python

Este projeto é um sistema simples de gerenciamento de tarefas.

## Estrutura
- `gerenciador/tarefas.py`: controla tarefas
- `gerenciador/usuarios.py`: controla usuários
- `gerenciador/relatorios.py`: gera relatórios
- `main.py`: menu principal

### Tipos de manutenção a aplicar:
- Corretiva: corrigir erros no código
- Perfectiva: melhorar ou completar funcionalidades
- Adaptativa: ajustar compatibilidade e padrões
- Preventiva: melhorar código e documentação para evitar problemas futuros

### Histórico de manutenção

Bugs encontrados na análise do sistema:

1. `adicionar_tarefa` não coloca a tarefa na lista, então nada está sendo salvo.
   Tipo: Corretiva

2. Concluir tarefa grava "Sim" em vez de `True`, então o relatório vai sempre tá mostrando 0 tasks concluídas.
   Tipo: Corretiva

3. Concluir e remover pegam a tarefa errada (digitar 1 pega a segunda). Digitar uma letra fecha o programa.
   Tipo: Corretiva

4. a função `listar_tarefas` está mostrando cada tarefa duas vezes e também tem uma função duplicada (`listar_tarefas_duplicada`).
   Tipo: Preventiva

5. A função `autenticar` existe no projeto mas não está sendo usada no menu, ou seja, não tem como fazer login.
   Tipo: Perfectiva

Outros pontos (Adaptativa):
- Os dados estão sumindo quando o programa fecha
- A senha é guardada sem proteção
- E também o `requirements.txt` está vazio

## Como executar
```bash
python main.py
```
