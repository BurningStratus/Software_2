"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. 
Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". 
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. 
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, 
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. 
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein 
sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

"""

from random import randint

highest_odometer = 0




class Car:
    list_cars = []

    def __init__(self, plate, top_speed, odo_km=0, curr_speed=0):
        self.plate = plate
        self.top_speed = top_speed
        self.curr_speed = curr_speed
        self.odo_km = odo_km

    def show_car(self):
        print(f"All units be advised: vehicle {self.plate} has a top speed of {self.top_speed} km/h!"
              f" ODO: {self.odo_km} km // Speedometer: {self.curr_speed} km/h.\n")
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
        
        if difference_km < 0:
            self.odo_km += -difference_km
            # print(f"{self.plate} slows down")
            return self.odo_km
        else:
            # print(f"The {self.plate} was tasked to drive for 1 hour @{delta} km/h.")
            self.odo_km += difference_km
            # print(f"In the end of the trip, the odometer shows {self.odom} km.\n")
            return self.odo_km

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


for contender in range(10):
    plate = "DEMDER-" + str(contender + 1)
    top_speed = randint(100, 200)

    Car.list_cars.append(Car(plate, top_speed))

suuri_romuralli = Demolition_derby("Suuri Romuralli", 8000, Car.list_cars)

print(f"\n{suuri_romuralli.name}\n")

race = True

cntr = 0

while race:
    suuri_romuralli.each_hour()
    
    cntr += 1
    
    if cntr % 10 == 0:
        suuri_romuralli.print_situation() 

    if suuri_romuralli.stage_completion() == True:
        race = False
        break

Car.list_cars.sort(key= lambda x: x.odo_km, reverse=True)

# print(Car.list_cars)

suuri_romuralli.print_situation()

#for car in Car.list_cars:
#    print(f"{car.plate} :: {car.odo_km} km")
