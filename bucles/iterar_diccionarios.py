diccionario = {
    "nombre":"Mirco",
    "apellido":"calle",
    "subs":1000000
}
#recorriendo un diccionario con items para obtener la clave y el valor
for key in diccionario.items(): #nos devuelve tuplas de datos
    print(key)
    
#como el key nos da un par de valores entonces podemos escribir de la siguiente manera
for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"la clave es: {key} y el valor es: {valor}")
    
