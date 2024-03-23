# GerenciadorTarefas
 Este código é uma aplicação de gerenciamento de tarefas usando a biblioteca Tkinter para a interface gráfica. Aqui está uma descrição do que ele faz:

1. Define duas classes: `Tarefa` e `ListaDeTarefas`.
   - `Tarefa`: Representa uma tarefa com uma descrição e um status de conclusão.
   - `ListaDeTarefas`: Mantém uma lista de tarefas e fornece métodos para adicionar, remover, marcar como concluída, mostrar, salvar e carregar tarefas.

2. Define funções para interagir com a interface gráfica:
   - `adicionar_tarefa()`: Adiciona uma nova tarefa à lista de tarefas.
   - `remover_tarefa()`: Remove a tarefa selecionada da lista de tarefas.
   - `marcar_como_concluida()`: Altera o status de conclusão da tarefa selecionada.
   - `atualizar_lista_tarefas()`: Atualiza a exibição da lista de tarefas na interface gráfica.
   - `salvar_tarefas()`: Salva as tarefas em um arquivo usando pickle e exibe uma mensagem de confirmação.

3. Configura a janela principal da aplicação com elementos de interface gráfica:
   - Entrada de tarefa.
   - Lista de tarefas.
   - Botões para adicionar, remover, marcar como concluída e salvar tarefas.

4. Inicializa uma instância da classe `ListaDeTarefas`, carrega as tarefas de um arquivo (se existir) e atualiza a exibição da lista de tarefas na interface gráfica.

5. Executa a aplicação, exibindo a janela principal e aguardando interações do usuário.
esta aplicação permite ao usuário adicionar, remover, marcar como concluída e salvar tarefas de uma lista, tudo através de uma interface gráfica simples.
