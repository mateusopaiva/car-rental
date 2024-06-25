cars = [
    ("Chevrolet Tracker", 120), 
    ("Chevrolet Onix", 90), 
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85), 
    ("Hyundai Tucson", 120), 
    ("Fiat Uno", 60), 
    ("Fiat Mobi", 70), 
    ("Fiat Pulse", 130)
]

def show_car_list(car_list):
    for i, car in enumerate(car_list):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))
