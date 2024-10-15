#creando un conjunto con set

conjunto = set(["dato 1", "dato 2"])

#los set no son modificables, es decir que no podemos poner una lista dentro del set,
#pero si vamos a poner una tupla
conjunto =set(["dato 1",("datoenlista1","datoenlista2")])

#metiendo un conjunto dentro de otro conjunto
# conjunto1 = { "dato1","dato2"}
# conjunto2 = {conjunto1,"dato3"}
#no se puede meter un conjunto dentro de otro conjunto de la manera anterior,
#para eso se utiliza frozenset()

conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#decimos conjutno 2 es subconjunto de conjunto 1?
resultado = conjunto2.issubset(conjunto1)

#otra forma en ves del issubset ponemos <=
resultado = conjunto2 <= conjunto1

#verificamos si es un superconjunto 
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 >= conjunto2

#verificamos si hay algun numero en comun, isdisjoint me da si son distinto
# si solo hubiera un solo dato que sea igual entonces me dara falso

resultado = conjunto2.isdisjoint(conjunto1) 

print(resultado)