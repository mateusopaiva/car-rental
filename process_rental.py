from cars import show_car_list
from utils import clear_screen

rented  = []

def process_rental(cars, rented):
    show_car_list(cars)
    print("==========")
    print("Escolha o código do carro:")
    car_code = int(input())
    print("Por quantos dias você deseja alugar este carro?")
    days  = int(input())
    clear_screen()

    print("Você escolheu {} por {} dias.".format(cars[car_code][0], days))
    print("O aluguel totalizaria R$ {}. Deseja alugar?".format(days * cars[car_code][1]))

    print("0 - SIM | 1 - NÃO")
    conf = int(input())
    
    if conf == 0:
        print("Parabéns você alugou o {} por {} dias.".format(cars[car_code][0], days))
        rented.append(cars.pop(car_code))
