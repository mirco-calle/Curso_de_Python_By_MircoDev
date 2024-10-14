#listas, las que estan entre []
lista = ["lucas dalto","soy dalto",True,1.85]
lista[1]="soy mirco"
print(lista[1])

#tuplas  (no se puede modificar)


tuple=("lucas dalto","soy dalto",True,1.85)
# tupla[1]="soy mirco"   no se puede modificar como las listas
#las que estan entre ()
tuple[0]
print(tuple)

#creando un conjunto (set)
#son como las tuplas no se pueden modificar
#no me permite repetir valores 
# conjunto [3] no podemos acceder al elemento por el indice como se hacen con las listas o tupla 
#no alamacena datos duplicados
conjunto = {"lucas dalto","soy dalto",True,1.85}  
print(conjunto)

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)

diccionario = {
    'nombre' : "lucas dalto",
    'canal': "soy dalto",
    'esta_emocionado': True,
    'altura':1.85,
    'dato duplicado' : "soy dalto"
}
print(diccionario['altura']+1)
print(lista[3])