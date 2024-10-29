# falto el profe y los pibes van a armar la clase
# 1 alumno es profesor
#1 alumno es asistente
#A) pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
#B) el mayor de la clase es el profesor y el menor es el asistente Quien es quien?

#Solucion:
#pedir el nombre y la edad de los compañeros que vinieron hoy a la clase
def obtener_companieros(cantidad_de_compas):
    #CREANDO UNA LISTA CON LOS COMPAÑEROS
    companieros = []
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compas):
            nombre = input('ingrese el nombre del compa: ')
            edad = int(input('ingrese la edad del compa: '))
            compa = (nombre,edad)
            
            #agregando la informaciona la lista
            companieros.append(compa)
    #oredenandolos de menor a mayor segun su edad        
    #key es un parametro opcional 
    companieros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir a asistente y a la profesor
    asistente = companieros[0][0]
    #[(1,2),(1,2),(1,2)]
    profesor = companieros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor
#desempaquetamos lo que nos retorna la funcion 
asistente,profesor =obtener_companieros(5)

#mostrando el resultado
print(f'el profesor es: {profesor} y su asistente es {asistente}' )