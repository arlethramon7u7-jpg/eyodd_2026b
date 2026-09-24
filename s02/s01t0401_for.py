"""
Escribir un programa que calculé 
la suma de los "n" números naturales 
por ejeplo si n = 100, el programa 
calculará la suma del 1 al 100
"""

#Importamos biblioteca time
import time

#Funcion que suma los
#primeros "n" numeros naturales
def sum_of_n(n):
    total_sum = 0
    #Sumando los "n" numeros
    #Ciclo for
    for number in range(1,n+1):
      total_sum = total_sum + number
    #Retornando el total de la suma
    return total_sum

#Variable para guardar
#El data set
dataset = [] # [(n,time,sum),(n,time,sum)]

#Generando el contenido del Dataset
for repetition in range(1,11):
  # Tomando el tiempo (inicial)
  timestamp_01 = time.time()

  # Sumo los "n" numeros
  n = repetition*500
  # Guardo el resultado en result
  result = sum_of_n(n)

  # ⏱️Tomando el tiempo final 
  timestamp_02 = time.time()

  # Calculando el tiempo
  elapsed_time = round ((timestamp_02-timestamp_01) * 1e6,2)

  # Agregar la tripleta de los 
  # datos al dataset
  dataset.append( (n,elapsed_time,result) )

# Imprimir el dataset
for tup in dataset:
   print(tup)

