"""
Generators

Los generadores son funciones que pueden
pausar su ejecuciòn.

Cuando se invoca una funcion generadora
devuelve un objeto generador (aka Interador).

El codigo dentro de la funcion no se ejecuta
de inmediato, solo se copila.

La funcion se ejecuta unicamente cuando 
iteras(repetir) sobre el generador.

"""

def my_generator():
    yield 1 # producir
    yield 2
    yield 3
    yield 4
    
# Se invocafuncion generadora
my_iterator = my_generator()

# Se itera manualmente sobre el generador 
#print(next(my_iterator)) # Imprime 1
#print(next(my_iterator)) # Imprime 2
#print(next(my_iterator)) # Imprime 3
#print(next(my_iterator)) # Imprime 4
#print(next(my_iterator)) # Imprime ?

# Los iteradores se pueden usar en un bucle for
for value in my_iterator:
    print(value)
