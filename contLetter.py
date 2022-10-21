frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra para contar en su frase: ')
cont = 0

for letter in frase:
    if letter == letra:
        cont += 1

print('La letra "{}" se ingreso {} veces'.format(letra, cont))