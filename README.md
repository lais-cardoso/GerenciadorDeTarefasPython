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

1 Correção Corretiva: Lógica e Tipagem
O erro mais grave estava na função total_tarefas, que tentava somar booleanos/strings, e na função concluir_tarefa, que usava uma string em vez de um valor booleano consistente.

O Erro: soma += t["concluida"] falha se o valor for uma string ("Sim").
d
A Solução: Padronizar o status como True/False e usar a função sum() do Python, que é mais eficiente.


2 Correção Perfectiva: Estrutura de Dados e Redundância
O código original tinha loops duplicados e não salvava as tarefas de fato na lista global.

O Erro: A função adicionar_tarefa apenas imprimia o texto, mas não dava um append na lista tarefas.

A Solução: Implementar a inserção real e remover loops repetidos na listagem.

## Como executar
```bash
python main.py