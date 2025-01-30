#para listas y tuplas y conjuntos exepto el "range" despues funciona igual
animales = ["gato","perro","loro","cocodrilo","pes"]
numeros = [10,62,12,45,50]

#reccoriendo la lisa animales
for animal in animales:   
    print(f'ahora la variabla animal es: {animal}')

#reccorriendo la lista numeros y multiplicarlo por 10
for numero in numeros:  
    resultado = numero *10
    print(resultado)
    
#iterando ambas listas juntas, con la funcion zip podemos recorer 2 listas al mismo tiempo y del mismo tamaño
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1 {animal}')
    print(f'recorriendo lista 2 {numero}')

#otra forma es utilizando range que itera solo hasta el rango entre dos numeros cualquiera en este caso elejimos 5 y 10  
for num in range(5,10):
    print(num)
    
#forma No optima de recorrer un alista NO FUNCIONA EN CONJUNTOS 
for num in range(len(numero)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
print(f'el indice es:{indice} y el valor es:{valor}')

#usando el else, siempre se muestra una sola vez aunque no haya valores
for num in numeros:
    print(num)
else:
    print('el bucle termino')
    
