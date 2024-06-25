from cars import show_car_list

def process_return(cars, rented):
    if len(rented) == 0:
        print("Não há carros para devolver.")
    else:
        print("Segue a lista de carros alugados. Qual você deseja devolver?")
        show_car_list(rented)
        print("")
        print("Escolha o código do carro que deseja devolver:")
        cod = int(input())
        print("Obrigado por devolver o carro {}".format(rented[cod][0]))
        cars.append(rented.pop(cod))
