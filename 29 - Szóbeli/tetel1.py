
def prim(szam):
    if szam < 2:
        return False
    
    for oszto in range(2, szam):
        if szam % oszto == 0:
            return False
    
    return True

print(prim(7))
print(prim(9))