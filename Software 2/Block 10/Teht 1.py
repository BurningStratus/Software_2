# Prog using class "elevator", which shows adjascent floors
# elevator can move one floor at a time and shows current floor
# there are 5 floors.

class Elevator:
    def __init__(self, floor=0):
        self.floor = floor

    def curr_floor(self):
        if 5 > self.floor > 0:
            print(f"UP:   [{self.floor + 1}]")
            print(f"DOWN: [{self.floor - 1}]")
        elif self.floor == 0:
            print(f"UP:   [{self.floor + 1}]")
        elif self.floor == 5:
            print(f"DOWN: [{self.floor - 1}]")

        print(f"You are at [{self.floor}]")
        return

    def goto(self, fl_num):
        if self.floor == fl_num:
            print(f"You are already at {self.floor}th floor.")
        elif fl_num <= 5:
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


elev1 = Elevator()

print("You step into the elevator. Type UP to go one level up, DOWN to go one level down, "
      "or floor number to go to [5, 4, 3, 2, 1, 0]."
      " Type 'step out' to end the 'journey'.")

cmd = "STARTER"

while cmd:

    elev1.curr_floor()
    cmd = input(":> ")

    if cmd.upper() == "STEP OUT":
        cmd = False
    elif cmd == "":
        continue
    elif cmd.upper() == "UP":
        elev1.floor_up()
    elif cmd.upper() == "DOWN":
        elev1.floor_down()
    elif int(cmd) == 0 or int(cmd) == 1 or int(cmd) == 2 or int(cmd) == 3 or int(cmd) == 4 or int(cmd) == 5:
        elev1.goto(int(cmd))
    else:
        print("whut???")
