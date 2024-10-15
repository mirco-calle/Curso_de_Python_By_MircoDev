cadena1 = 'hola soy dalto'
cadena2 = "buenvenido a la clase"
cadena3 = "HOLA SOY MIRCO"
cadena4 = "4"
cadena5 = "asdfsdfsdf"
cadena6 = "hola,soy,mirkex"

#dato.metodo()   es la estructura de un metodo

#convertimos a mayuscula
resultado = cadena1.upper()

#convertimos en minuscula
resultado = cadena3.lower()

#primera letra en mayuscula
primer_letra_mayus = cadena1.capitalize()

#bucamos una cadena en otra cadena, encuentra la posicion de la letra que le pedimos,
#si no hay considencias devuelve -1
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena, a deferencia de find cuando 
# no encuentra una considencia, devulve un excepcion
busqueda_index = cadena1.index("a")

# si es numerico , devolvemos true, si no devuelve false, pero el dato tiene que ser una cadena
es_numerico = cadena4.isnumeric()

# si es alfanumerico devolvemos true sino devolvemos false solo de la A a la Z
es_alfanumerico = cadena5.isalpha()

# contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("soy")

#contamos cuantos caracteres tiene una cadena, OJO no es un metodo es una funcion
#en caso de ponerle un Array este cuenta el numero de datos en el Array
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es as devuelve true
empieza_con = cadena1.startswith("h")

# verificamos si una cadena termina con otra cadena dada, si es as devuelve true
termina_con = cadena1.endswith("to")

#remplaza un pedazo de la caeena dada, por otra dada
#si el valor 1 se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("Hola","carambas")

#separar cadenas con la cadena que la pasemos y los convierte en una lista
cadena_separada = cadena6.split(",")

print(contar_caracteres)
