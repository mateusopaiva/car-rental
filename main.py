from cars import show_car_list
from process_rental import process_rental
from process_return import process_return
from utils import display_menu

def main():
    from cars import cars
    from process_rental import rented

    while True:
        op = display_menu()

        if op == 0:
            show_car_list(cars)

        elif op == 1:
            process_rental(cars, rented)

        elif op == 2:
            process_return(cars, rented)

        print("")
        print("===========")
        print("0 para CONTINUAR | 1 para SAIR")
        if float(input()) == 1:
            break

if __name__ == "__main__":
    main()
