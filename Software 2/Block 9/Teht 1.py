
class Car:
    def __init__(self, plate, top_speed, curr_speed=0, odom=0):
        self.plate = plate
        self.top_speed = top_speed
        self.curr_speed = curr_speed
        self.odom = odom

    def show_car(self):
        print(f"All units be advised: an unidentified car {self.plate} has a top speed of {self.top_speed} km/h!"
              f" It went {self.odom} km already at {self.curr_speed} km/h!")
        return None


car1 = Car("ABC-123", 142)
Car.show_car(car1)
