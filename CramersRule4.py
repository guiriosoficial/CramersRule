# Calculadora de Determinante de Matriz de Ordem 4 (4x4) utilizando regra de cramer
#
#

matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for line in range(0, 4):
    for column in range(0, 4):
        matrix[line][column] = int(input(f'Insira o valor do índice [{line}, {column}]: '))

print(matrix)