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

GRUPO 03 / Larissa Almeida, Leonardo Macena, Pedro Gregori /

Arquivo : tarefas.java

1. O código não guarda as tarefas na lista, pois a função de adicionar tarefa só mostra uma mensagem e não salva a tarefa de verdade.

2. A função que mostra as tarefas é repetida, ou que faz o programa mostrar a mesma lista duas vezes.

3. Não existe nenhuma função para mostrar os usuários, ou seja, está faltando essa parte no código.

4. O campo que diz se a tarefa é feito ou não usa um valor de verdadeiro ou falso, e isso deveria ser usado para facilitar o controle.

5. O código usa texto ("Sim") para marcar a tarefa como concluída, mas isso pode causar confusão. O ideal é usar um valor verdadeiro ou falso.

6. A função que deveria mostrar apenas as tarefas que são repetidas é mostrar todas as tarefas, mesmo que não sejam repetidas.

7. Por causa disso, uma lista de tarefas repetidas não está funcionando direito e mostra tudo.

8. O código não permite realmente concluir as tarefas, pois não muda o estado delas corretamente quando tenta marcar como concluído.

9. A função para remover tarefas não corrige corretamente o índice passado e, por isso, não remove a tarefa da lista como esperado.

10. O código não valida se os campos foram preenchidos, permitindo que fiquem vazios.


ARQUIVO: relatório.java

1. O relatório não apresenta mensagem de validação para o caso de lista vazia

2. Como as tarefas não são marcadas como concluídas no código, o relatório não mostra corretamente quais tarefas foram concluidas, comprometendo a precisão das informações exibidas para o usuário.

ARQUIVO: usario.java

1. O sistema permite cadastrar o mesmo usuário várias vezes, pois não há nenhuma seleção para evitar duplicatas. 

2. O cadastro do usuário deve ser feito antes das tarefas, respeitando a ordem lógica e hierárquica dos processos.

MELHORIAS IMPLEMENTADAS:

1. Corrigida a função de adicionar tarefas para salvar realmente as tarefas.

2. Strings substituídas por valores booleanos para status.

3. Renomeado o campo "concluído" para "status".

4. Removida a duplicidade na impressão da lista de tarefas.

5. Ajustada a verificação para concluir as tarefas corretamente.

6. Fizemos teste de unidade em cada campo modificado

## Como executar
```bash
python main.py