#utilizando el operador * como parametro (*args)
def suma(nombre, *numeros):
    return f"{nombre} la suma de tus numeros es:{sum(numeros)}"
resultado = suma('mirco',4,5,6,7)
print(resultado)

#otra forma seria, la forma mas optima
def suma_total(numeros):
    return f'otra forma seria {sum([*numeros])}'
resultado2 = suma_total([4,5,6,7])

print(resultado2)