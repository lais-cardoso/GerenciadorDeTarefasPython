# Gerenciador de Tarefas Python

Este projeto é um sistema simples de gerenciamento de tarefas.

## Estrutura
- `tarefas.py`: controla tarefas
- `usuarios.py`: controla usuários
- `relatorios.py`: gera relatórios
- `main.py`: menu principal

# Erros
- Função de adicionar tarefas não adiciona a lista 
- Função morta nomeada "doc_ruim"
- Existe a função de buscar tarefa no arquivo "tarefas.py", porém não está sendo chamada no menu, além de não ser cidada no README
- Existe a função de mostrar o total de tarefas concluidas no arquivo "tarefas.py" nomeada incorretamennte "total_tarefas", e não está sendo chamada no menu, além de não ser cidada no README
- Função de remover tarefa não indica qual tarefa foi removida, apenas a mensagem de que foi removida

## Execução
### Tipos de manutenção a aplicar:
- Corretiva: corrigir erros no código
- Evolutiva: adicionar funcionalidades novas
- Preventiva: melhorar código e documentação
- Adaptativa: ajustar compatibilidade e padrões

### Histórico de manutenção

GRUPO 03: Larissa Almeida, Leonardo Macena, Pedro Gregori 

ARQUIVO : tarefas.py

1. - Corretiva: O código não guarda as tarefas na lista, pois a função de adicionar tarefa só mostra uma mensagem e não salva a tarefa de verdade.  ✔️ Corrigido

2. - Preventiva: A função que mostra as tarefas é repetida, ou que faz o programa mostrar a mesma lista duas vezes. ✔️ Corrigido

3. - Evolutiva: Não existe nenhuma função para mostrar os usuários, ou seja, está faltando essa parte no código. ✔️ Corrigido

4. - Corretiva: O campo que diz se a tarefa foi concluída, não usa um valor de verdadeiro ou falso, e isso deveria ser usado para facilitar o controle. ✔️ Corrigido

5. - Preventiva: O código usa texto ("Sim") para marcar a tarefa como concluída, mas isso pode causar confusão. O ideal é usar um valor verdadeiro ou falso. ✔️ Corrigido

6. - Preventiva: A função que deveria mostrar apenas as tarefas que são repetidas é mostrar todas as tarefas, mesmo que não sejam repetidas. ✔️ Corrigido

8. - Corretiva: O código não permite realmente concluir as tarefas, pois não muda o estado delas corretamente quando tenta marcar como concluído. ✔️ Corrigido

9. - CorretivaA função para remover tarefas não corrige corretamente o índice passado e, por isso, não remove a tarefa da lista como esperado. ✔️ Corrigido

10. - Preventiva: O código não valida se os campos foram preenchidos, permitindo que fiquem vazios.

11. - Evolutiva: Validação para remover tarefas quando não houve tarefas, foi observado que pede o número de tarefas mesmo não tendo nenhuma era para ser interrompido logo no começo.

12. - Preventiva: Permite colocar qualquer caracter e não avisa que é permitido apenas número inteiros. 


ARQUIVO: relatório.py

1. - Evolutiva: O relatório não apresenta mensagem de validação para o caso de lista vazia. ✔️ Corrigido

2. - Preventiva: Como as tarefas não são marcadas como concluídas no código, o relatório não mostra corretamente quais tarefas foram concluidas, comprometendo a precisão das informações exibidas para o usuário. ✔️ Corrigido

ARQUIVO: usuario.py

1. - Preventiva: O sistema permite cadastrar o mesmo usuário várias vezes, pois não há nenhuma seleção para evitar duplicatas. 

2. - Preventiva: O cadastro do usuário deve ser feito antes das tarefas, respeitando a ordem lógica e hierárquica dos processos.

MELHORIAS IMPLEMENTADAS:

1. - Corretiva: Corrigida a função de adicionar tarefas para salvar realmente as tarefas. ✔️ Feito

2. - Preventiva: Strings substituídas por valores booleanos para status. ✔️ Feito

3. - Preventiva: Renomeado o campo "concluído" para "status". ✔️ Feito

4. - Preventiva: Removida a duplicidade na impressão da lista de tarefas. ✔️ Feito

5. - Preventiva: Ajustada a verificação para concluir as tarefas corretamente. ✔️ Feito

6. Fizemos teste de unidade em cada campo modificado. ✔️ Feito

## Como executar
```bash
python main.py