def prim(szam):
    if szam < 2:
        return False
    
    if szam == 2:
        return True
    
    for oszto in range(3, szam):
        if szam % oszto == 0:
            return False
    
    return True

print(prim(7))
print(prim(9))