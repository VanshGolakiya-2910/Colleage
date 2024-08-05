from numpy import gcd

def fill_the_water(jug):
    jug[0] = jug[1]

def empty_the_water(jug):
    jug[0] = 0

def transfer(jugA, jugB):
    remain = jugB[1] - jugB[0]
    transfer_amount = min(jugA[0], remain)
    jugA[0] -= transfer_amount
    jugB[0] += transfer_amount

# Initialize the jugs and goal
a = [0, int(input("Enter the value of jug having higher capacity: "))]
b = [0, int(input("Enter the value of jug having lower capacity: "))]
goal = int(input("Enter the desired value of Goal: "))

# Check if the goal can be achieved
if goal % gcd(a[1], b[1]) == 0:
    while not (b[0] == goal or a[0] == goal):
        if a[0] == 0:
            fill_the_water(a)
            print(f"({a[0]}, {b[0]})")
        transfer(a, b)
        print(f"({a[0]}, {b[0]})")
        if b[0] == b[1]:
            empty_the_water(b)
            print(f"({a[0]}, {b[0]})")
else:
    print("Solution Not Possible")
