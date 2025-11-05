# Gerenciador de Tarefas Python

Este projeto é um sistema simples de gerenciamento de tarefas.

## Funcionalidades
- Adicionar tarefas
- Listar tarefas
- Concluir tarefas
- Remover tarefas
## erro
ERROS
- 1 fui tentar adicionar uma tarefa e a terefa nao estava adicionando CORRETIVA
- 2 função lista tarefa esta duplicada 17 a 20 CORRETIVA
- 3 função concluir tarefa esta errada esta com sim mas o correto e true/false PREVENTIVA
- 4 linhas 23 26 30 e 33 estao ignorando erros e concluido mesmo estando erados PREVENTIVA
- linha 45 erro na soma esta somando tudo e deveria somar somente as concluidas PREVENTIVA
- linhas 48 funcao sem sentido ADAPTATIVA
- funcoes desnecesarias de a a g nao foram utilizadas em nenhum momento ADAPTATIVA
- linha 52 funcao inutil ADAPTATIVA
## CORECOA
- corrigir remover e concluir tarefa que nao estava dando erro na indice estava dando indice invalida
- corrigir adicionar tarefa que estava adicionando mesmo os campos estando vazios
- corrigir erro no cadastrastro ususario que estava cadastrando com os campos em brancos 
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

