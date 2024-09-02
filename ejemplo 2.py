def ordenar_fila(matriz, fila):
  """Ordena una fila específica de una matriz en orden ascendente utilizando el algoritmo de inserción.

  Args:
    matriz: La matriz bidimensional a modificar.
    fila: El índice de la fila a ordenar.
  """
  for i in range(1, len(matriz[fila])):
    valor_actual = matriz[fila][i]
    j = i - 1
    while j >= 0 and matriz[fila][j] > valor_actual:
      matriz[fila][j + 1] = matriz[fila][j]
      j -= 1
    matriz[fila][j + 1] = valor_actual

# Crear una matriz de ejemplo
matriz = [[1, 5, 3],
          [8, 4, 3],
          [2, 7, 5]]

# Imprimir la matriz original
print("Matriz original:")
for fila in matriz:
  print(fila)

# Ordenar la segunda fila (índice 1)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Imprimir la matriz con la fila ordenada
print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz:
  print(fila)