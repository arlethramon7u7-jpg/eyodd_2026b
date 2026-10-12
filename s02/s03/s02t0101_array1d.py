# Array
#from array import *
import array as arr

# Creacion de un arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Numero decimal
# d: Numero decimal doble
# u: Carácteres unicode
my_array = arr.array("i",[10,22,300,3,7,
40,55,80,700,654,34])

# Iteracion automatica
# for num in my_array:
# print(num)

# Acceso individual a los elementos
# print(my_array[0]) # Primer elemento 
# print(my_array[1]) # Segundo elemento 
# print(my_array[2]) # Tercer elemento 

# Tamaño de un areglo
# Length
# print(len(my_array))

# Interacion por indices
for i in range(len(my_array)):
    if my_array[i] % 2 == 0:
      print(f"Elemento Num {i+1}:{my_array[i]}")



