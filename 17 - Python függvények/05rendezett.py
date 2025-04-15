def szetbonto(szoveg, elvalaszto=","):
    lista = szoveg.split(elvalaszto)
    lista.sort
    return lista

print(szetbonto("alma,körte,dió,mogyoró"))
print(szetbonto("szilva-eper-barack-dinnye", "-"))