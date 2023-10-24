import random


class Car:
    def __init__(self, plate, top_speed, odom=0, curr_speed=0):
        self.plate = plate
        self.top_speed = top_speed
        self.curr_speed = curr_speed
        self.odom = odom

    def show_car(self):
        print(f"All units be advised: an unidentified vehicle {self.plate} has a top speed of {self.top_speed} km/h!"
              f" ODO: {self.odom} km // Speedometer: {self.curr_speed} km/h.\n")
        return None

    def speed_change(self):
        '''

        :return:
        '''
        delta = random.randint(-10, 15)

        if self.curr_speed + delta > self.top_speed:
            # print(f"current speed can't be > {self.top_speed} km/h!")
            # print(f"the {self.plate} has reached its top speed.\n")
            self.curr_speed = self.top_speed
            return delta
        elif self.curr_speed + delta < 0:
            # print(f"speed can't be < 0 km/h!")
            self.curr_speed = 0
            return delta
        else:
            self.curr_speed += delta
            return delta

    def drive(self, delta):
        if delta < 0:
            self.odom += -delta
            # print(f"{self.plate} slows down")
            return self.odom
        else:
            # print(f"The {self.plate} was tasked to drive for 1 hour @{delta} km/h.")
            self.odom += delta
            # print(f"In the end of the trip, the odometer shows {self.odom} km.\n")
            return self.odom

    def finish(self):
        pass

cars = []

for plates in range(1, 11):
    lic_plate = "ABC-" + str(plates)
    car_i = "car_" + str(plates)
    cars.append([car_i, lic_plate, random.randint(100, 200)])

#print(cars)
'''
cars = [('ABC-1', 198), ('ABC-2', 102), ('ABC-3', 164), 
        ('ABC-4', 191), ('ABC-5', 146), ('ABC-6', 152), 
        ('ABC-7', 107), ('ABC-8', 171), ('ABC-9', 154), 
        ('ABC-10', 147)]
'''

highest_odometer = 0
while highest_odometer <= 10000:
    for car in cars:
        car[0] = Car(car[1], car[2])
        delt = car[0].speed_change()

        # print(car)

        car[2] += int(car[0].drive(delt))
        # print(car[2])

        if car[2] > highest_odometer:
            highest_odometer = car[2]

cars.sort(key=lambda x: x[2], reverse=True)
# print(cars)

for car_loop in sorted(cars, key=lambda x: x[2], reverse=True):
    print(car_loop[1:3])

