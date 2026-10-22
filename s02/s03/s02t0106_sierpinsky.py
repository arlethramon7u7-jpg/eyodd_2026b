from array import array as arr # Renombra en nombre de la biblioteca 

# Parametros de mi cuadricula
rows = 3
columns = 2 * rows - 1

# Creando el frid 2D
matrix = []
# Construyendo el grid
for _ in range(rows):
    new_row = arr("i",[0] * columns)
    matrix.append(new_row) # Append = Insertar datos

# Validando la construccion del Grid
print(f"Cantidad de filas: {len(matrix)}") 
print(f"Cantidad de columnas: {len(matrix[0])}")

for rows in matrix:
  print(list(rows))
