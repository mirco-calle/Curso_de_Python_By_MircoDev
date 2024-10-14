
# a) diferencia en porcentaje entre el curso actual y 
#  -el mas rapido de otros cursos
#  - el mas lento de otros cursos
#  -el promedio de los cursos
# b) porcentaje de material inservivle que se reduce en:
# -el promedio de los cursos
# -el curso actual
# c) ver 10 horas de este curso a cuantas de otros curso equivale? y al reves?

#datos
#promedio de duraciones
otros_curso_min = 2.5
otros_curso_max = 7 
otros_curso_promedio = 4
mirco_curso = 1.5

#duracion de crudo, el video sin editar
crudo_promedio = 5
crudo_mirco =3.5


#diferencia de duracion

diferencia_con_min = 100-(mirco_curso/otros_curso_min *100)
diferencia_con_max = 100-(mirco_curso/otros_curso_max *100)
diferencia_con_promedio = 100-(mirco_curso/otros_curso_promedio *100)

#calculando el % de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_curso_promedio/crudo_promedio*100
tiempo_vacio_mirco = 100 - mirco_curso/crudo_mirco*100



print ("-------------------------")
print(f'el curso de dalto dura un{diferencia_con_min}% menos que el mas rapido de los cursos')
print(f'el curso de dalto dura un {diferencia_con_max}% menos que el mas lento de los cursos')
print(f'el curso de dalto dura un {diferencia_con_promedio}% menos que el promedio de los otros cursos')

print ("-------------------------")
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"este curso elimino {tiempo_vacio_mirco}% de tiempo vacio")

#aqui simplemente usamos la regla de 3
print ("-------------------------")
print(f"ver 10 horas de este curso equivale a ver {otros_curso_promedio/mirco_curso*10} horas de otros cursos")
#al reves
print(f"ver 10 horas de otros cursos equivale a ver {mirco_curso/otros_curso_promedio * 10} horas de este curso")