numeros = [4,7,1,42,15]
# encontrando el nuemro mayor de una lista, peude ser una tupla o un conjunto
numero_mas_alto=max(numeros)
print(numero_mas_alto)

#encontrando un numero menor de una lista 
numero_mas_alto=min(numeros)
print(numero_mas_alto)

#redondeando a 6 decimales, se le agrega con una coma para indicarle cuantos decimales queremos
numero_redondeado = round(12.346546,2)
print(numero_redondeado)

#funcion bool retorna False si le damos como argumento-> 0 ,vacio,False, nunguno
#nos retorna True si le pasamos un numero distinto de 0, cadena , o datos no vacios , lista
resultado_bool = bool(-1)
print(resultado_bool)

#funcion all , retorna true si todos los valores son verdaderos, Ejm 0, none, vacio, son falsos
resultado_all = all([0,"true",[244,55]])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)