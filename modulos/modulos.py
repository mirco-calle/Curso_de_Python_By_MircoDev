import modulo_saludar 

#la funcion saludar aqui pasa a ser un metodo
saludo=modulo_saludar.saludar('juan')
print(saludo)

#otra forma es cambiando de nomre al modulo con "as"
import modulo_saludar as m_saludar

#la funcion saludar aqui pasa a ser un metodo
saludo=m_saludar.saludar('juan')
print(saludo)

#si solamente queremos importar una funcion en especifico hacemos:
from modulo_saludar import saludar

saludo2=saludar('roberta')
print(saludo2)

#importando mas de una funcion 
from modulo_saludar import saludar,saludar_raro

saludar=saludar('ramona')
saludo3=saludar_raro('ramiro')
print(saludo3)

#podemos cambiar el nombre a nuestras funciones tambiencon "as"
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_rarisimo

saludar=saludar_normal('ramona')
saludo3=saludar_rarisimo('ramiro')
print(saludo3)

# no confundir al importar variables de funciones, a las funciones se las llama con letra mayuscula al principio