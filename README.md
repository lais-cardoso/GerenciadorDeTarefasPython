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
    1. Corretiva: Ajustar a função de concluir e deletar tarefas para seguirem o ID da tarefa na função, ao invés de seguir o índice da lista.
    2. Corretiva: Ajustar a função de criar tarefas para as tarefas criadas aparecerem na lista de tarefas.
    3. Preventiva: Remover a função duplicada de listar tarefas.
    4. Preventiva: Alterar o uso de "Sim" para "Concluída" quando uma tarefa foi concluída para prevenir confusão.
    5. Perfectiva: Adicionar a função de listar os usuários no menu, facilitando assim encontrar quem são os usuários que estão "logados".
    6. Perfectiva: Verificar se o campo de título de descrição estão preenchidos.
    7. Adaptativa: Não foi possível encontrar
    8. Adaptativa: Não foi possível encontrar

## Como executar
```bash
python main.py
	
