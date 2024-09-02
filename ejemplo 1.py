def buscar_valor_en_matriz(matriz, valor_buscado):


  for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
      if matriz[fila][columna] == valor_buscado:
        return fila, columna
  return None

# Crear una matriz de ejemplo
matriz = [[1, 3, 5],
          [7, 9, 11],
          [13, 15, 17]]

# Valor a buscar
valor_buscado = 7

# Realizar la búsqueda
resultado = buscar_valor_en_matriz(matriz, valor_buscado)

# Mostrar los resultados
if resultado:
  fila, columna = resultado
  print(f"El valor {valor_buscado} se encontró en la posición ({fila}, {columna})")
else:
  print(f"El valor {valor_buscado} no se encontró en la matriz.")