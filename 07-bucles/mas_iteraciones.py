frutas = ["banana","manzana","ciruela","pera","granada","durazno"]
cadena = "hola mirco"
numeros = [2,3,4,5,6]
#evitando que se coma una granada con la sentencia "continue"
for fruta in frutas:
    if fruta =="granada":
      continue
    print(f'me voy a comer una {fruta}')
    
#evitar que el bucle siga ejecutandose con "break" el else tampoco se ejecuta
for fruta in frutas:
    if fruta == 'pera':
     break
    print(f'Me voy a comer una {fruta}')
print("bucle terminado")

#recorrer un acadena de texto
for letra in cadena:
    print(letra)

#bucles en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

