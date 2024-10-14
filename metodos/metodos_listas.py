#creando un alista con list, OJO no es un metodo es una funcion
lista = list(["hola","dalto",34])

lista2 = list([1,8,3,40,5,6,True,False])
#devuelve la cantidad de elementos de la lista
camtiodad_elementos = len(lista)

#agregando un elemento a la lista, desde aqui ya no usamos como variable sino que afectamos a la lista solamente
lista.append("jajajaja")

#agregando un elemento a la lista en un indice especifico, primero ponemos la posicion y luego el dato
lista.insert(2,"toma mama")

#agregando varios elementos a la lista, lo agrgamos en corchetes porque le estamos pasando una lista 
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice)
#si quiero eliminar el ultimo elemento de la lista entonces se pone "-1" para eliminar el ultimo
#-2 para eliminar el antepenultimo de la la lista y asi sucesivamente
lista.pop(1)
lista.pop(-2)

#removiendo un elemento de la lista por su valor
lista.remove("toma mama")

#ordenando la lista de forma ascendente  (si usamos el parametro reverse=True lo ordena en reversa)
lista2.sort()
lista2.sort(reverse=True)

#inviertiendo los elementos de una lista
lista2.reverse()

#verificando si un elemento se encuentra en la lista 
elemento_encontrado = lista2.index(True)
# eliminando todos los elementos de la lista 
#lista.clear()
print(lista2)
print(elemento_encontrado)