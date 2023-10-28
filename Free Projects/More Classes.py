
class Owner:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.garage = []

    def buy_car(self, car_instance):
        self.garage.append(car_instance)
        print(f" I'm {self.f_name} {self.l_name} and I bought a {car_instance.model}.")
        return

    def showoff(self):
        print(f"\nHi there, I'm {self.f_name} and here's what I have:\n")
        for car in self.garage:
            car.car_review()


class Car:
    def __init__(self, maker, model, year, engine_displacement):
        self.maker = maker
        self.model = model
        self.year = year
        self.eng_dsplcmnt = engine_displacement

    def car_review(self):
        print(f"{self.maker} {self.model} {self.year} {self.eng_dsplcmnt}L.")
        return


class Service:
    def __init__(self):
        pass


def car_sell(old_ownr, new_ownr, car_instance):
    old_ownr.garage.remove(car_instance)
    new_ownr.garage.append(car_instance)
    print(f"{car_instance.maker} {car_instance.model} is now owned by {new_ownr.f_name} {new_ownr.l_name}")
    return


buick_roadmaster = Car("Buick", "Roadmaster", 1993, 5.7)
crown_victoria = Car("Ford", "Crown Victoria", 1987, 6.4)
dodge_stratus = Car("Dodge", "Stratus", 1995, 2.5)
holden_hq = Car("Holden", "Sonara HQ", 1972, 5.8)
chevy_elcamino = Car("Chevrolet", "El Camino", 1989, 3.5)
volvo_740 = Car("Volvo", "740", 1990, 2.4)


# easy_find[any_car.model] = any_car
# print((easy_find['Roadmaster']).year)
# buick_roadmaster.car_review()

datadict = buick_roadmaster.__dict__

dude_1 = Owner("Tyler", "Durden")
dude_2 = Owner("Max", "Cohen")
dude_3 = Owner("Jack", "Pierce")

owners = [dude_1.f_name, dude_2.f_name, dude_3.f_name]
car_lineup = [buick_roadmaster, crown_victoria, holden_hq, dodge_stratus]

for car in car_lineup:
    Car.car_review(car)
    qqq
for dude in owners:
    pass

input(" <ENTER> ")

dude_1.buy_car(crown_victoria)
dude_2.buy_car(dodge_stratus)
dude_2.buy_car(buick_roadmaster)
dude_3.buy_car(holden_hq)
dude_3.buy_car(volvo_740)
dude_2.buy_car(chevy_elcamino)

cmd = ""
while cmd != "STOP":
    pass
    cmd = "STOP"