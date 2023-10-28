'''
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
'''
from numpy import inf


class House:
    amt = 0

    def __init__(self, high_floor, ground_floor):
        self.high_floor = high_floor
        self.ground_floor = ground_floor
        self.id = id
        self.amt_of_elev = 0
        self.list_of_elev = []
        House.amt += 1

    def add_elevator(self, new_elev):

        self.list_of_elev.append(new_elev)
        self.amt_of_elev = len(self.list_of_elev)

        for elevator in self.list_of_elev:
            # gives elevators info about amount of floors.
            elevator.hi_floor = self.high_floor
            elevator.low_floor = self.ground_floor

    def elevat_goto(self, elev, target_floor):
        elev.curr_floor()
        elev.go_to(target_floor)


class Elevator:
    amt_elev = 0

    def __init__(self, floor=0):
        self.floor = floor
        self.hi_floor = 0
        self.low_floor = 0
        Elevator.amt_elev += 1

    def curr_floor(self):

        if self.hi_floor > self.floor > self.low_floor:
            print(f"UP:   [{self.floor + 1}]")
            print(f"DOWN: [{self.floor - 1}]")
        elif self.floor == self.low_floor:
            print(f"UP:   [{self.floor + 1}]")
        elif self.floor == self.hi_floor:
            print(f"DOWN: [{self.floor - 1}]")

        print(f"You are at [{self.floor}]")
        return

    def go_to(self, fl_num):
        if self.floor == fl_num:
            print(f"You are already at {self.floor}th floor.")
        elif self.low_floor <= fl_num <= self.hi_floor:
            self.floor = fl_num
        return

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        print(f"You are at [{self.floor}]")

        if self.floor > 0:
            self.floor -= 1
        else:
            print("You are already at 0th floor.")


house1 = House(inf, 0)
house2 = House(5, 1)

print(House.amt)

elev1 = Elevator()
elev2 = Elevator()
elev3 = Elevator()
elev4 = Elevator()
elev5 = Elevator()

house1.add_elevator(elev1)
house1.add_elevator(elev3)
house2.add_elevator(elev2)
house2.add_elevator(elev4)
house2.add_elevator(elev5)

listof_houses = [house1, house2]

cmd_lift = cmd_house = " "


while cmd_house:

    cmd_lift = True

    print(len(listof_houses))

    choice = int(input(f"Choose a house [1 - {len(listof_houses)}]\n:>"))
    house_in_play = listof_houses[choice - 1]

    # print(listof_houses[choice-1].listof_elev)

    choice = int(input(f"Choose the elevator [{len(house_in_play.list_of_elev)}]\n:>"))

    print(f"You are at {choice}, {house_in_play} house")

    # print(choose_house)
    chosen_elev = house_in_play.list_of_elev[choice - 1]


    print("You step into the elevator. Type UP to go one level up, DOWN to go one level down, "
          f"or floor number to go to [{house_in_play.ground_floor} - {house_in_play.high_floor}]."
          " Type 'step out' to end the 'journey'.")

    while cmd_lift != "stepout":
        chosen_elev.curr_floor()
        cmd_lift = input(":> ")
qqq
        try:
            cmd_lift = int(cmd_lift)
            chosen_elev.go_to(int(cmd_lift))
        except:
            if cmd_lift.upper() == "STEP OUT":
                cmd_lift = "stepout"
            elif cmd_lift.upper() == "UP":
                chosen_elev.floor_up()
            elif cmd_lift.upper() == "DOWN":
                chosen_elev.floor_down()
            else:
                print("whut???")
