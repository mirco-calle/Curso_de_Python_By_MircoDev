numeros = [1,2,3,4,5,6,7,8,9]

#lambda es como crear una funciones anonimas, para ahorrarnos bloque de codigo
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(4))

#creando funcion comun que diga si es par o no 
def es_par(num):
    if (num%2==0):
        return True

#usando filter con una funcion comun, usa la funcion es_par y pasale los numeros
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))

#creando lo mismo que antes pero con lambda

numeros_pares = filter(lambda num:num%2 == 0,numeros)
print(list(numeros_pares))
