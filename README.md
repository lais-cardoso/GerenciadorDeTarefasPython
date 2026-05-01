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

### Felipe e Miguel

#### Corretiva:
 - função adicionar_tarefa não estava adicionando tarefa (corrigido)
 - função listar_tarefas não estava saindo quando a lista estava vazia (corrigido)

#### Preventiva:
 - função gerar_relatorio fazendo comparações desnecessarias (corrigido)
 - função main com muitos if, mudei para switch (corrigido)

#### Adaptativa:
 - função listar_tarefas tem um for desnecesasrio (corrigido)
 - função gerar_relatorio agora usa listar_tarefas_concluidas (corrigido)

#### Evolutiva:
 - função total_tarefa nome errado, agora é total_tarefas_concluidas (corrigido)
 - função listar_tarefas_desnecessarias (corrigido)

## Como executar
```bash
python main.py