szamok = range(1, 101)

for elem in szamok:
    if elem % 15 == 0:
        print("FizzBuzz", end=", ")
    elif elem % 5 == 0:
        print("Buzz", end=", ")
    elif elem % 3 == 0:
        print("Fizz", end=", ")
    else:
        print(elem, end=", ")

print()
