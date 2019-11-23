# Calculadora de Determinante de Matriz de Ordem 4 (4x4) utilizando regra de cramer
#
#

print('Insira a Matrix 4x4 separada por ESPAÇO e ENTER:')
matrix = [list(map(int, input().split()))for i in range(4)]

for line in range(4):
    for column in range(4):
        print(f'{matrix[line][column]:^5}', end=' ')
    print()


# f'Insira o valor do índice [{line}, {column}]: '
