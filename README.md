# Gerenciador de Tarefas (Python)

Aplicativo simples em linha de comando para gerenciar tarefas.

## Funcionalidades
- Adicionar tarefas
- Listar tarefas
- Concluir tarefas
- Remover tarefas
## Erros
- Variáveis inutilizadas.
- Parâmetro inutilizado.
- Ausência de return na função "listar_tarefa", para evitar o loop desnecessário, após a linha 18.
- Ausência do parâmetro "título" na função "concluir_tarefa" para exibir a tarefa específica que foi concluída.
- Uso desnecessário de try/catch. O melhor é usar if/else, uma vez que try/catch é usado para tratar erros que são imprevisiveis em tempo de execução.


## Execução
```bash
python main.py