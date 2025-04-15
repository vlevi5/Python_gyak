sakktabla = [
    ["B", "L", "F", "K", "N", "F", "L", "B"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["B", "L", "F", "K", "N", "F", "L", "B"],
]

def kirajzol(sakktabla):
    for sor in sakktabla:
        for babu in sor:
            if babu == "X":
                print(" \t", end="")
            else:
                print(f"{babu}\t", end="")
        print()

kirajzol(sakktabla)