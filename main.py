# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def getN():
    n = 0
    while n < 1:
        try:
            n = int(input('Введите количество уравнений (обязательно равное количеству переменных): '))
        except ValueError as e:
            print("Ошибка ввода, попробуйте ещё раз")
    return n


def getMatrix(n):
    matrixA = [[]] * n
    print('Введите элементы матрицы СЛАУ (без столбца свободных членов)')

    for i in range(n):
        matrixA[i] = list(map(int, input().split()))

    matrixB = []

    print('Введите столбец свободных членов')
    cin = input()
    if len(cin.split()) == 1:
        matrixB.append(float(cin))
        for i in range(1, n):
            matrixB.append(float(input()))
    else:
        matrixB = list(map(float, cin.split()))

    return matrixA, matrixB


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def solve(matrixA, matrixB):
    n = len(matrixA)
    matrixR = [0] * n
    for i in range(n):
        matrixR[i] = [0] * n
    matrixL = [0] * n
    for i in range(n):
        matrixL[i] = [0] * n

    for i in range(n):
        matrixR[i][i] = 1

    for i in range(n):
        for j in range(n):
            cur = matrixA[j][i]
            for k in range(n):
                cur -= matrixL[j][k] * matrixR[k][i]
            matrixL[j][i] = cur / matrixR[i][i]

        for j in range(i+1, n):
            cur = matrixA[i][j]
            for k in range(n):
                cur -= matrixL[i][k] * matrixR[k][j]
            matrixR[i][j] = cur / matrixL[i][i]

    matrixZ = [0] * n
    matrixX = [0] * n
    matrixZ[0] = matrixB[0]/matrixL[0][0]


    for i in range(1, n):
        sum = 0
        for k in range(0, i):
            sum += matrixL[i][k] * matrixZ[k]
        matrixZ[i] = (matrixB[i] - sum) / matrixL[i][i]


    matrixX[n-1] = round(matrixZ[n-1],9)

    for i in range(n-2, -1, -1):
        sum = 0
        for k in range(i+1, n):
            sum += matrixR[i][k]*matrixX[k]
        matrixX[i] = round(matrixZ[i] - sum, 9)

    for i in range(n):
        print(f'X{i+1} = {matrixX[i]}')



def test():
    matrixA = [
        [5, 7, 6, 5],
        [7, 10, 8, 7],
        [6, 8, 10, 9],
        [5, 7, 9, 10],
    ]
    matrixB = [23, 32, 33, 31]
    solve(matrixA, matrixB)

def main():
    matrixA, matrixB = getMatrix(getN())
    solve(matrixA, matrixB)

main()
input()
# test()