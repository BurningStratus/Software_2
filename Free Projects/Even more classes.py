### Assosiations in classes
class Student:

    count = 0

    def __init__(self, name, age=0):  # age oletusarvo 15, jossei määritelty kutsussa
        self.name = name
        self.age = age
        self.credits = 0
        Student.count += 1
        print(f"New student added. [{Student.count}]")

    def say_hello(self):
        print(f"Hi there. {self.name}, {self.age}. "
              f"I got {self.credits} credits.")

    def change_name(self, new_name):
        self.name = new_name

    def add_credits(self, credits):
        # estä opintopisteiden meneminen negaativiseksi
        if self.credits + credits < 0:
            self.credits = 0
        else:
            self.credits = self.credits + credits


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def checkcursname(self):
        print(f"curs name is {self.name}")

    def checkstudents(self):
        for all_students in self.students:
            print(f"{all_students.name} enrolled")

    def give_credits(self, credit_units):
        for student in self.students:
            student.add_credits(credit_units)
            student.say_hello()


class School:
    def __init__(self, name, location):
        self.course = []
        self.students = []
        self.name = name
        self.location = location

    def printer_name(self):
        print(f"You are at {self.name}")

    def add_course(self, course_new):
        self.course.append(course_new)

    def enrollment(self, student):
        self.students.append(student)


metropol = School("Metropolia", "Karaportti")
laurea = School("Laurea", "Leppavaara")


st1 = Student("Henry Stickmin", 38)
st1.add_credits(30)

st2 = Student("Rob Zombie", 58)
st2.add_credits(23)

st3 = Student("Michael Jackson", 40)
st3.add_credits(50)

st4 = Student("Britney Spar", 38)
st4.add_credits(30)

st5 = Student("Rob Zombie", 58)
st5.add_credits(23)

st6 = Student("Michael Jackson", 40)
st6.add_credits(50)


st1.say_hello()
st2.say_hello()
st3.say_hello()

print(f"Hi there. There are {Student.count} students.")

math = Course("Meth")
physics = Course("Fisiks")

# Rob does Meth
# Michael does Fisiks
# Henry does both

math.add_student(st1)
math.add_student(st2)

physics.add_student(st2)
physics.add_student(st3)

math.checkstudents()
physics.checkstudents()

metropol.add_course(math)
metropol.add_course(physics)

metropol.enrollment(st1)
metropol.enrollment(st2)
metropol.enrollment(st3)

laurea.enrollment(st4)
laurea.enrollment(st5)
laurea.enrollment(st6)

laurea.add_course(math)
laurea.add_course(physics)

# TODO Fire Drill: All students have to ran away from the school.
