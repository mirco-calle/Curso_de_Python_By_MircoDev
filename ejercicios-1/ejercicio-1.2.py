#a) pedirle al usuario que diga cualquier texto real y:
#-calcular cuanto tardaria en decir esa frase
#-cuantas palabras dijo?
#b) si se tarda mas de 1 minuto:
# -decirle: "para tampoco te pedi un testamento"

#c) Mirco habla un 30% mas rapido: 
# cuanto tardaria el en decirlo?

frase = input("Dime un frase y te calculo cuanto tardarias si tuvieras que decirla")

#calculamos la cantidad de palabras que tiene una frase con el metodo Split

palabras_separadas = frase.split(" ")

cantidad_de_palabras = len(palabras_separadas)

print(f'dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo ')

if cantidad_de_palabras >120 :
    print('para tampoco te pedi un testamento')
    
