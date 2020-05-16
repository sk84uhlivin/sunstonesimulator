import random


print()


def rolls():
    roll1 = random.randint(25, 65)
    roll2 = random.randint(25, 65)
    roll3 = random.randint(25, 65)
    roll4 = random.randint(25, 65)
    return roll1, roll2, roll3, roll4


a, b, c, d = rolls()

if a + b >= 100:
    print(f"Crystal 1: {a}")
    print(f"Crystal 2: {b}")
    print()
    print("2 Crystal!")
elif a + b + c >= 100:
    print(f"Crystal 1: {a}")
    print(f"Crystal 2: {b}")
    print(f"Crystal 3: {c}")
    print()
    print("3 Crystal!")
else:
    print(f"Crystal 1: {a}")
    print(f"Crystal 2: {b}")
    print(f"Crystal 3: {c}")
    print(f"Crystal 4: {d}")
    print("4 crystal!")
