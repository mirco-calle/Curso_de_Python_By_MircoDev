#creando una funcion simple
def saludar():
    print("hola como estas")

saludar()

#funcion con parametros, un parametro es un variable, tambien llamado argumento en otros lenguajes
def saludar2(nombre,sexo):
    if(sexo=='mujer'):
        adjetivo = 'reyna'
    elif(sexo=='hombre'):
        adjetivo='titan'
    else:
        adjetivo='amor'

    print(f'hola {nombre}, mi {adjetivo} como estas?')

saludar2('sandra','mujerr')

#crear una funcion que nos retorne valores
def sumando (a,b):
    suma = a+b
    #print(suma)
    return suma
    
suma = sumando(3,5)
print(suma)

#otro ejemplo que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = 'qscefbrthm'
    num_entero = str(num)
    num = int(num_entero[0])
    c1=num-2
    c2=num
    c3=num-5
    contraseña=f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contraseña,num
# aqui aplicamos desempaquetar la funcion 
pasword, primer_numero= crear_contraseña_random(52342)
frase = f'tu contra es: {pasword}'
frase2 = f'tu numero es: {primer_numero}'
#mostrando los resultados obtenidos
print(frase)
print(frase2)
    
    


