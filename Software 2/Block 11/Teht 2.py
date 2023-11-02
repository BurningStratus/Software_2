
from random import randint
from math import fabs as abs

highest_odometer = 0

class Car:
    list_cars = []

    def __init__(self, plate, top_speed, odo_km=0, curr_speed=0):
        self.plate = plate
        self.top_speed = top_speed
        self.curr_speed = curr_speed
        self.odo_km = odo_km

    def car_info(self):
        print(f"vehicle {self.plate}   // Top speed: {self.top_speed} km/h."
              f" ODO: {self.odo_km} km // Speedometer: {self.curr_speed} km/h.")
        return None

    def speed_change(self):

        velocity_diff = randint(-10, 15)

        if self.curr_speed + velocity_diff > self.top_speed:
            # print(f"current speed can't be > {self.top_speed} km/h!")
            # print(f"the {self.plate} has reached its top speed.\n")
            self.curr_speed = self.top_speed
            return velocity_diff
        elif self.curr_speed + velocity_diff < 0:
            # print(f"speed can't be < 0 km/h!")
            self.curr_speed = 0
            return velocity_diff
        else:
            self.curr_speed += velocity_diff
            return velocity_diff

    def drive(self, difference_km):
        diff_km = abs(difference_km)
        
        # print(f"The {self.plate} was tasked to drive for 1 hour @{delta} km/h.")
        self.odo_km += diff_km
        # print(f"In the end of the trip, the odometer shows {self.odom} km.\n")
        return self.odo_km

class ICE(Car):
    def __init__(self, plate, top_speed, fuel_consumption, tank_l, odo_km=0, curr_speed=0):
        super().__init__(plate, top_speed, odo_km, curr_speed)
        self.fuel_consumption = fuel_consumption / 100
        self.tank_capacity = tank_l
        self.tank_actual = tank_l

    def car_info(self):
        print(f"\nvehicle {self.plate} Top speed: {self.top_speed} km/h"
              f" ODO: {self.odo_km} km // Speedometer: {self.curr_speed} km/h."
              f" Tank: {self.tank_actual} L // Fuel consumption: {self.fuel_consumption *100} L/100 km")
        return
    
    def drive(self, difference_km):
        diff_km = abs(difference_km)
        
        # print(f"The {self.plate} was tasked to drive for 1 hour @{delta} km/h.")
        self.odo_km += diff_km
        self.tank_actual = self.tank_actual - (diff_km * self.fuel_consumption)
        # print(f"In the end of the trip, the odometer shows {self.odom} km.\n")
        
        return self.odo_km, self.tank_capacity
    
    


class ELEC(Car):
    def __init__(self, plate, top_speed, power_kwh, capacity_kwh, odo_km=0, curr_speed=0):
        super().__init__(plate, top_speed, odo_km, curr_speed)
        self.power_kwh = power_kwh / 100
        self.capacity_kwh = capacity_kwh
        self.capacity_actual = capacity_kwh

    
    def car_info(self):
        print(f"vehicle {self.plate} Top speed: {self.top_speed} km/h"
              f" ODO: {self.odo_km} km // Speedometer: {self.curr_speed} km/h."
              f" Battery: {self.capacity_actual} kWh Power: {self.power_kwh * 100} kWh/100 km")
        return

    def drive(self, difference_km):
        diff_km = abs(difference_km)
        # print(f"The {self.plate} was tasked to drive for 1 hour @{delta} km/h.")
        self.odo_km += diff_km
        self.capacity_actual = self.capacity_actual - (diff_km * self.power_kwh)
        # print(f"In the end of the trip, the odometer shows {self.odom} km.\n")
        return self.odo_km, self.capacity_kwh


class Demolition_derby:
    def __init__(self, name: str, distance_km: int, contenders_list: list):
        self.name = name
        self.distance_km = distance_km
        self.contenders_list = contenders_list
        
    def participate(self, contender):
        self.contenders_list.append(contender)

    def each_hour(self):
        
        for contender in self.contenders_list:
            
            speed_diff = contender.speed_change()
            contender.odo_km += contender.drive(speed_diff)

        return
    
    def print_situation(self):
        for contender in self.contenders_list:
            print(f"{contender.plate} @{contender.curr_speed}km/h odometer:{contender.odo_km}")
        
        return

    def stage_completion(self) -> bool:
        
        for contender in sorted(self.contenders_list, key= lambda obj: obj.odo_km, reverse=True):
            if contender.odo_km >= self.distance_km:
                print(f"\n{contender.plate} has finished!\n")
                return True
            else:
                continue
        else:
            return False

"""
for contender in range(10):
    plate = "DEMDER-" + str(contender + 1)
    top_speed = randint(100, 200)

    Car.list_cars.append(Car(plate, top_speed))
"""
suuri_romuralli = Demolition_derby("Suuri Romuralli", 8000, Car.list_cars)
#print(f"\n{suuri_romuralli.name}\n")

race = False  #### Set to True to start the race 
cntr = 0
while race:
    suuri_romuralli.each_hour()
    
    cntr += 1
    
    if cntr % 10 == 0:
        suuri_romuralli.print_situation() 

    if suuri_romuralli.stage_completion() == True:
        race = False
        break
#Car.list_cars.sort(key= lambda x: x.odo_km, reverse=True)
#suuri_romuralli.print_situation()

holden_hq = ICE("R0AD-M4STR", 165, 32.4, 32.4, 160000)
tesla_x = ELEC("ELON-SPAM", 185, 23.4, 52.5, 3000)

holden_hq.car_info()
tesla_x.car_info()

print(holden_hq.drive(3000))
print(tesla_x.drive(3000))

holden_hq.car_info()
tesla_x.car_info()