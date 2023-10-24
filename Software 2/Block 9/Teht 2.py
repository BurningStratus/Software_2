class Car:
    def __init__(self, plate, top_speed, curr_speed=0, odom=0):
        self.plate = plate
        self.top_speed = top_speed
        self.curr_speed = curr_speed
        self.odom = odom

    def show_car(self):
        print(f"All units be advised: an unidentified vehicle {self.plate} has a top speed of {self.top_speed} km/h!"
              f" It went {self.odom} km already at {self.curr_speed} km/h!\n")
        return None

    def speed_change(self, delta):
        if self.curr_speed + delta > self.top_speed:
            print(f"current speed can't be > {self.top_speed} km/h!")
            print("the car has reached its top speed.")
            self.curr_speed = self.top_speed
            return None
        elif self.curr_speed + delta < 0:
            print(f"speed can't be < 0 km/h!")
            self.curr_speed = 0
            print("the car has fully stopped.")
            return None
        else:
            self.curr_speed += delta
            print(f"Current speed is {self.curr_speed} km/h now.")


car1 = Car("ABC-123", 142)
Car.show_car(car1)

Car.speed_change(car1, 30)
Car.show_car(car1)

Car.speed_change(car1, 50)
Car.show_car(car1)

Car.speed_change(car1, 70)
Car.show_car(car1)

Car.speed_change(car1, -200)
Car.show_car(car1)
