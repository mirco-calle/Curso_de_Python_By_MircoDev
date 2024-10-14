diccionario ={
    "nombre" : "mirco",
    "apellido":"calle",
    "subs": 100000
}
#keys() => devuelve las claves (tambien nos sirve para iterar)
#nos devuelve un objeto dict_item
#claves = diccionario.keys()

#nos devuelve el valor, si no encuentra el valor nos devuelve "none" que no tiene valor y no asi una excepcion, es parecido al undefined de javascript
#obteniendo un elemento con get() (si no encuentra nada el programa continua)
#claves = diccionario.get("subs")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del dicconario
diccionario.pop("subs","nombre")

#obteniendo un elemento dic_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

