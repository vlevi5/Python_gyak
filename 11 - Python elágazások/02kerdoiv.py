print("Válasszon ki egy helyes választ!")
print("Mennyi 2 + 2?")
print("a) 1")
print("b) 2")
print("c) 3")
print("d) 4")
print("e) 5 - 1")
print("f) 0 + 4")

valasz = input("A helyes válasz: ")

if valasz != "" and (valasz == "d" or valasz == "e" or valasz == "f"):
    print("A megadott válasz helyes! ")
else:
    print("A megadott válasz helytelen! ")