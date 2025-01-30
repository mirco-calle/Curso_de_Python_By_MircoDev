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

#si nuestro archivo esta dentro de una carpeta, entonces el codigo es el siguiente 
from funciones_buenas.modulo_saludar2 import saludar_funcion

saludarUltimo = saludar_funcion('mirco')

print(saludarUltimo)
#ahora si quiero sacar todo el modulo no solo una funcion 
import funciones_buenas.modulo_saludar2

print(funciones_buenas.modulo_saludar2.saludar_funcion('victor'))

#ahora como el nombre de la importacion es muy largo le ponemos alias "as"

import funciones_buenas.modulo_saludar2 as m_saludoUltimo

print(m_saludoUltimo.saludar_funcion("Eliot"))

#que pasa si el modulo no esta dentro de la carpeta 'modulos" esta afuera
#llamamos a la carpeta funciones_afuera con sys que es una funcion construido en python es decir 'built-in'
import sys 

sys.path.append("D:\\MircoDev\\CURSO DE PYTHON\\curso de python Dalto\\funciones_afuera")

import saludo
print(saludo('Roberta'))
