from utils import clear_screen

def display_menu():
    clear_screen()
    print("===============================")
    print("Bem vindo à locadora de carros!")
    print("===============================")
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    
    while True:
        try:
            op = int(input())
            if op in [0, 1, 2]:
                return op
            else:
                print("Opção inválida. Por favor, digite 0, 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")