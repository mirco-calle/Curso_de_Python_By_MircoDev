#creando un afuncon de 3 paramnetros
def frase (nombre,apellido,adjetivo):
    return f'hola {nombre} {apellido}, eres muy {adjetivo}'

frase_resultante = frase('Mirco','Calle','Sabio')
print(frase_resultante)

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo='tonto'):
    return f'hola {nombre} {apellido}, eres muy {adjetivo}'
frase_resultante = frase('Mirco','Calle','intelignete')
print(frase_resultante)