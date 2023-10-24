
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

    def drive(self, time_h):
        print(f"The car was tasked to drive for {time_h} hours @60 km/h.")
        self.odom += 60 * time_h
        print(f"In the end of the trip, the odometer shows {self.odom} km.")


car1 = Car("ABC-123", 142, 104655)
Car.show_car(car1)

Car.drive(car1, 1.5)
