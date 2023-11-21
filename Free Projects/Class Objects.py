import random
### Classes

names = []
inventories = [["Apple", "Banana", "Pen", "AK-47"], ["Pineapple", "Cocoa", "Beer", "AWP"]]


def give_credits(c_redit):
    c_redit = random.randint(0, 10)
    return c_redit


class Student:

    def __init__(self, name, age, credit):
        self.name = name
        self.age = age
        self.credits = credit

    def say_hello(self):
        print(f"Hi there. Im {self.name}, {self.age} y.o, and I have {self.credits} credits.")

    def woof(self, times):
        for i in range(times):
            print("Woof-woof!")

    def addtolist(self, name, age, creds):
        names.append((name, age, creds))


for integ in range(1000):
    rand = random.randint(0, 10)
    namn, age = input("Student:>"), int(input("Age:>"))
    st1 = Student(namn, age, rand)
    st1.say_hello()
    st1.woof(rand)
    st1.addtolist(namn, age, rand)
    print(names)
    print(st1)
    print(Student.__qualname__)

