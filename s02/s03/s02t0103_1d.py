# Importando duncion Array
# del 

from array import array as arr

# Importando una funcion de otro
# Archivo
from s02t0102_1d import print_array 

my_array = arr("i",[2,10,15,20])

print("---ANTES DE LA INSERCION---")
print_array(my_array)

# Insercion
my_array.insert(1,90)
print("---DESPUES DE LA INSERCION---")
print_array(my_array)

print ("--DESPUES DE UN APPEND---")
my_array.append(1000)
print_array(my_array)

print("---SIMULAR UN APPEND CON INSERT---")
my_array.insert(len(my_array),90000)
print_array(my_array)
