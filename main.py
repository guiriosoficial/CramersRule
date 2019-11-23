# Cramer Rule Matrix Systems Calculator and Laplace Theorem
# Cramer's Rule | Xi = det(Ai) / det(A)
# Laplace       | Sum cof(A)i*j * A(i*j)
# Cofactor      | (-1)^i+j * det(A)i*j


def laplace(matrix, index_val=1):
    # Set the matrix length
    n = len(matrix)

    # Return Det if Matrix length is 1
    if n == 1:
        return index_val * matrix[0][0]
    else:
        sign = -1
        det = 0
        for i in range(n):
            mtx = []
            for j in range(1, n):
                buff = []
                for k in range(n):
                    if k != i:
                        buff.append(matrix[j][k])
                mtx.append(buff)
            sign *= -1
            det += index_val * laplace(mtx, sign * matrix[0][i])
        return det


def cramer(matrix, results, order):
    # Calc and Show Main Matrix Determinant
    main_det = laplace(matrix)
    print(f'\nDeterminante da matrix principal: {main_det}')

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
            print(f'\nMatriz com substituição na COLUNA {r + 1}:')
            for line in matrix_sub:
                for num in line:
                    print(f'{num:^6}', end=' ')
                print()

            # Calc Determinant with Substitution
            sub_det = laplace(matrix_sub)
            print(f'Determinante igual a {sub_det}')

            # Calc and Save Final Resolution
            resolution.append(sub_det / main_det)

    # Return Resolution to Display in Main
        return resolution

    # Display Resolution if Main Det is 0
    else:
        return 0


def main():
    # Read Matrix Range
    order = int(input('Insira a Ordem da Matriz: '))

    # Read Matrix Numbers
    print(f'Insira a Matrix {order}x{order} formatada com ESPAÇO (Colunas) e ENTER (Linhas):')
    matrix = [list(map(float, input().split())) for i in range(order)]

    # Read Matrix Results
    results = list(map(float, input('Insira os resultados separados por ESPAÇO: ').split()))

    # Show Mounted Matrix
    print('\nSeu sistema completo é:\n')
    for l, line in enumerate(matrix):
        for num in line:
            print(f'{num:^6}', end=' ')
        print(f'= {results[l]:^6}', end='\n')

    # Define if Has Correct Data
    reset = input('\nOs dados estão corretos? (Y/n): ').lower()
    if reset == 'n':
        print(), main()
    else:
        # Show Final Results
        resolution = cramer(matrix, results, order)
        if resolution != 0:
            print('\nConjunto de soluções:')
            for r in range(order):
                print(f'A{r + 1} = {resolution[r]}')
        else:
            print('\nImpossivel finalizar algorítmo.\nA determinante da matriz principal é IGUAL a 0.')


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
# def Cramer(matrix):
#     n = len(matrix)
#     mainMat = []
#     for i in range(n):
#         mainMat.append([])
#         for j in range(n):
#             mainMat[i].append(matrix[i][j])
#     mainDet = det(mainMat)
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
#             print('x', r+1, '=', det(nowMat) / mainDet)
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
# Cramer(matrix)
