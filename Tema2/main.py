import numpy as np


def pivot(A, i, n):
    maxVal = -np.inf
    maxIndex = -1
    for j in range(i, n):
        if abs(A[j][i]) > maxVal:
            maxVal = A[j][i]
            maxIndex = j
    return maxIndex


def swapLines(A, i, p):
    A[[i, p]] = A[[p, i]]
    return A


def solveSystem(A, n):
    result = [0] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += A[i][j] * result[j]
        result[i] = (A[i][n] - s) / A[i][i]
    return result


def Gauss(A, e, n):
    currentCol = 0
    p = pivot(A, 0, n)
    if p:
        A = swapLines(A, 0, p)
    while (currentCol < n - 1) and abs(A[currentCol][currentCol]) > e:
        for i in range(currentCol + 1, n):
            A[i][currentCol] = A[i][currentCol] / float(A[currentCol][currentCol])
            for j in range(currentCol + 1, len(A[i])):
                A[i][j] -= A[i][currentCol] * A[currentCol][j]
        currentCol += 1
        p = pivot(A, currentCol, n)
        if p != currentCol:
            A = swapLines(A, currentCol, p)

    if p and abs(A[currentCol][currentCol]) <= e:
        print("Matrice singulara")
        return A, True

    return A, False


def tema(A, e, n):
    Ainit = [x[:n] for x in A]
    Binit = [x[n] for x in A]
    A = np.array(A, dtype='f')

    A, singular = Gauss(A, e, n)

    if singular:
        return

    xgauss = solveSystem(A, n)
    norm1 = np.linalg.norm(np.subtract(np.dot(Ainit, xgauss), Binit))
    xbibl = np.linalg.solve(Ainit, Binit)
    norm2 = np.linalg.norm(np.subtract(xgauss, xbibl))
    invAbibl = np.linalg.inv(Ainit)
    norm3 = np.linalg.norm(np.subtract(xgauss, np.dot(invAbibl, Binit)))

    AIn = np.concatenate((Ainit, np.identity(n)), axis=1)
    AIn, _ = Gauss(AIn, e, n)
    solutions = []
    for i in range(n, len(AIn[0])):
        deleteArray = list(range(n, len(AIn[0])))
        deleteArray.remove(i)
        k = np.delete(AIn, deleteArray, 1)
        solutions.append(solveSystem(k, n))
    AIn = np.transpose(solutions)

    norm4 = np.linalg.norm(np.subtract(AIn, invAbibl))

    print(f"Xgauss = {xgauss}")
    print(f"Norma ||Ainit * Xgauss - Binit||2 = {norm1}", ">=" if norm1 > e else "<", "10 ^ -6")
    print(f"Xbibl = {xbibl}")
    print(f"Norma ||Xgauss - Xbibl||2 = {norm2}", ">=" if norm2 >= e else "<", "10 ^ -6")
    print(f"A^-1bibl = {invAbibl}")
    print(f"Norma ||Xgauss - A^-1bibl * Binit||2 = {norm3}", ">=" if norm3 >= e else "<", "10 ^ -6")
    print(f"A^-1gauss= {AIn}")
    print(f"Norma ||A^-1gauss - A^-1bibl|| = {norm4}", ">=" if norm4 >= e else "<", "10 ^ -6")


if __name__ == '__main__':
    m = -6
    eps = 10 ** m
    matrix = [[2, 0, 1, 5], [0, 2, 1, 1], [4, 4, 6, 14]]
    # matrix = [[3, 1, 10], [5, -3, -2]]
    tema(matrix, eps, len(matrix[0]) - 1)
