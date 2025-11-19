# Gerenciador de Tarefas Python

Este projeto é um sistema simples de gerenciamento de tarefas.

## Funcionalidades
- Adicionar tarefas
- Listar tarefas
- Concluir tarefas
- Remover tarefas
## erro
ERROS
- 1 fui tentar adicionar uma tarefa e a terefa nao estava adicionando :CORRETIVA
- 2 função lista tarefa esta duplicada 17 a 20 :CORRETIVA
- 3 função concluir tarefa esta errada esta com sim mas o correto e true/false :PREVENTIVA
- 4 linhas 23 26 30 e 33 estao ignorando erros e concluido mesmo estando erados :PREVENTIVA
- linha 45 erro na soma esta somando tudo e deveria somar somente as concluidas :PREVENTIVA
- linhas 48 funcao sem sentido :ADAPTATIVA
- funcoes desnecesarias de a a g não foram utilizadas em nenhum momento :ADAPTATIVA
- linha 52 funcao inutil foi removida :PERFECTIVA

## Estrutura
- `tarefas.py`: controla tarefas
- `usuarios.py`: controla usuários
- `relatorios.py`: gera relatórios
- `main.py`: menu principal


# Histórico de manutenção

## Função adicionar tarefa:
- Erro 1 :  ao selecionar a primeira opção, o sistema exibe apenas "título", em vez da mensagem adequada solicitando o nome ou a descrição da tarefa. Corretiva

## Função Listar tarefas:
- Erro 2:  a linha 19 contém o mesmo código da linha 17, causando duplicidade e comportamento incorreto. CORRETIVA

- Erro 3 :ao tentar acessar a lista de tarefas, nenhum item é exibido.Corretiva

## Interatividade
- Erro 4: a opção 6 corresponde ao cadastro de usuários, o que não faz sentido dentro da posição atual do menu do gerenciador de tarefas.Perfectiva

## Função concluir tarefas:
- Errro 5: linhas 23, 26, 30 e 33 estão ignorando erros e marcando tarefas como concluídas mesmo quando há inconsistências. PREVENTIVA

## Função total_tarefas :
 -Erro 6: na linha 45, a função soma todas as tarefas, embora devesse somar apenas as concluídas. Corretiva

 ## Função Usuarios:
 -Erro 7 :o sistema permitia o cadastro de usuários com campos nulos, sem impedir o registro ou emitir mensagem de erro.Corretiva

 ## Função listar_tarefas_duplicadas
 -Erro 8: função inutilizada ,não tem utilidade. PERFECTIVA



## Correção
- Ajustada duplicação na listagem de tarefas.
- Corrigida a sintaxe responsável pela conclusão de tarefas.
- Corrigido o fluxo de cadastro de usuário, impedindo registro com campos nulos e adicionando mensagem de erro apropriada.

## Execução
### Tipos de manutenção a aplicar:
- Corretiva: corrigir erros no código
- Evolutiva: adicionar funcionalidades novas
- Preventiva: melhorar código e documentação
- Adaptativa: ajustar compatibilidade e padrões



## Como executar
```bash
python main.py
´´´


