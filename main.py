# Cramer Rule Matrix Systems Calculator and Laplace Theorem
# Cramer's Rule | Xi = det(Ai) / det(A)
# Laplace       | Sum cof(A)i*j * A(i*j)
# Cofactor      | (-1)^i+j * det(A)i*j


def det(matrix):
    return 6


def cramer(matrix, results, order):
    # Calc Main Matrix Determinant
    main_det = det(matrix)

    # Build New Matrix with Substitutions
    if main_det != 0:
        resolution = []
        for r in range(order):
            matrix_sub = []
            for i in range(order):
                matrix_sub.append([])
                for j in range(order):
                    if j == r:
                        matrix_sub[i].append(results[i])
                    else:
                        matrix_sub[i].append(matrix[i][j])

            # Show Actual Matrix with Substitution
            print(f'\nMatrix com Substituição na COLUNA {r + 1}:')
            for line in matrix_sub:
                for num in line:
                    print(f'{num:^6}', end=' ')
                print()

            # Calc Determinant with Substitution
            sub_det = det(matrix_sub)
            print(f'Determinante Igual a {sub_det}')

            # Calc and Save Final Resolution
            resolution.append(sub_det / main_det)

    # Return Resolution to Display in Main
        return resolution

    # Display Resolution if Main Det is 0
    else:
        print('A Determinante da Matriz Principal é IGUAL a 0.')


def main():
    # Read Matrix Range
    order = int(input('Insira a Ordem da Matriz: '))

    # Read Matrix Numbers
    print(f'Insira a Matrix {order}x{order} formatada com ESPAÇO (Colunas) e ENTER (Linhas):')
    matrix = [list(map(int, input().split())) for i in range(order)]

    # Read Matrix Results
    results = list(map(int, input('Insira os resultados separados por ESPAÇO: ').split()))

    # Show Mounted Matrix
    print('\nSeu sistema completo é:\n')
    for l, line in enumerate(matrix):
        for num in line:
            print(f'{num:^6}', end=' ')
        print(f'= {results[l]:^6}', end='\n')

    # Define if Has Correct Data
    reset = input('\nOs Dados estão corretos? (Y/n): ').lower()
    if reset == 'n':
        print(), main()
    else:
        resolution = cramer(matrix, results, order)

        # Show Final Results
        print('\nConjunto de Soluções:')
        for r in range(order):
            print(f'A{r + 1} = {resolution[r]}')


main()

# def det(matrix, mul = 1):
#     width = len(matrix)
#     if width == 1:
#         return mul * matrix[0][0]
#     else:
#         sign = -1
#         total = 0
#         for i in range(width):
#             m = []
#             for j in range(1, width):
#                 buff = []
#                 for k in range(width):
#                     if k != i:
#                         buff.append(matrix[j][k])
#                 m.append(buff)
#             sign *= -1
#             total += mul * det(m, sign * matrix[0][i])
#         return total
#
#
# def cramer(matrix):
#     n = len(matrix)
#     mainMat = []
#     for i in range(n):
#         mainMat.append([])
#         for j in range(n):
#             mainMat[i].append(matrix[i][j])
#     mainDet = det(mainMat)
#     print(mainMat)
#
#     if mainDet != 0:
#         for r in range(n):
#             nowMat = []
#             for i in range(n):
#                 nowMat.append([])
#                 for j in range(n):
#                     if j == r:
#                         nowMat[i].append(matrix[i][n])
#                     else:
#                         nowMat[i].append(matrix[i][j])
#     #         print('x', r + 1, '=', det(nowMat) / mainDet)
#             print(nowMat)
#
#
# print('Enter number of unknowns = n')
# n = int(input())
# print('sequentially enter the elements of matrix n*(n+1)')
# matrix = []
# for i in range(n):
#     matrix.append([])
#     for j in range(n + 1):
#         matrix[i].append(float(input()))
#
# print(len(matrix))
# cramer(matrix)
