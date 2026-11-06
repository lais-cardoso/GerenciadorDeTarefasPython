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

## Como executar
```bash
python main.py

-# Alterações

- Correção da função adicionar
- Foi criada uma nova opção para listar o usuário (antes era possível ver os usuários criados apenas depois de criar um novo)
- Na função "listar_usuarios():" agora exibe uma mensagem "Nenhum usuário cadastrado." caso nenhum usuário seja encontrado

-# Bugs e alterações encontrados e suas classificações

- A função adicionar tarefa não funciona (manutenção corretiva)

- Nova opção para listar usuários (manutenção perfectiva)

- É possível criar um usuário com o mesmo nome e senha (manutenção corretiva)
