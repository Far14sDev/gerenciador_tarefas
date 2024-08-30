# gerenciamento_tarefas.py

def adicionar_tarefa(lista_tarefas, tarefa):
    """Adiciona uma nova tarefa à lista de tarefas."""
    # Implementar a função aqui

def listar_tarefas ():
    print("Selecione o tipo de listagem:\n")
    print("|=========================================|")
    print("| 1 - Listar todas as tarefas             |")
    print("| 2 - Listar tarefas por prioridade       |")
    print("| 3 - Listar tarefas por categoria        |")
    print("| 4 - Sair                                |")
    print("|=========================================|")
    opc = int(input(": -> "))
    if opc == 1:
        for t in tarefas:
            print(t)
    elif opc == 2:
        select = int(input("Digite a prioridade: "))
        for i in tarefas:
            if i["prioridade"] == select:
                print(f"Tarefa: {i["nome"]}, Prioridade: {i["prioridade"]}")
    elif opc == 3:
        select = int(input("Digite a categoria: "))
        for i in tarefas:
            if i["categoria"] == select:
                print(f"Tarefa: {i["nome"]}, Categoria: {i["categoria"]}")
    elif opc == 4:
        return menu


def remover_tarefa(lista_tarefas, indice):
    """Remove uma tarefa da lista pelo índice."""
    # Implementar a função aqui

def main():
    tarefas = []
    while True:
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefas, tarefa)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            remover_tarefa(tarefas, indice)
        elif escolha == "4":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
