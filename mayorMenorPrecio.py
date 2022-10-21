listaPrecios = [50, 75, 46, 22, 80, 65, 8]
minimo = listaPrecios[0]
maximo = listaPrecios[0]

for precio in listaPrecios:
    if precio > maximo:
        maximo = precio
    elif precio < minimo:
        minimo = precio

print ("El menor precio es {} y el mayor es {}".format(minimo, maximo))