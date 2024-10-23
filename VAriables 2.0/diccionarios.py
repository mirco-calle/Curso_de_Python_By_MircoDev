#creando dicconarios con dict(), se crea como si fuera un objeto de javascript, la diferencia es que metemos = en ves de :
diccionario=dict(nombre="Mirco",apellido="calle")

#las listas [] NO PUEDEN, los conjuntos {} tampoco NO PUEDEN ser claves, la tuplas SI PUEDEN ser claves, aqui escribimos sin "dict"
#pero una lista[] con frozenset SI PUEDE, usamos para meter conjuntos
diccionario = {("mirco","bueno"):"jajaja"}
diccionario = {frozenset(['Mirco',"bueno"]):"jojojojo"}

#creamos diccionario con fromkeys que es un metodo de diccionario, en el ejemplo nos itera el nombre, es decir el primer dato es lo que vamos a 
#iterar, y el segunto se iguala a la iteracion, por defecto es None 
diccionario = dict.fromkeys("nombre","apellido")

#pero si colocamos como lista nos dara resultados "None", pero se puede cambiar
diccionario = dict.fromkeys(["nombre","apellido"])


print(diccionario["nombre"])


