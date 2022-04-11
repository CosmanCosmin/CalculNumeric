import numpy as np
import math
from copy import deepcopy


def determineMaxIndex(A, n):
    m, p, q = -1, -1, -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(A[i][j]) > m:
                m, p, q = abs(A[i][j]), i, j
    return p, q


def sign(x):
    return -1 if x < 0 else 1


def determineTheta(A, p, q):
    alpha = (A[p][p] - A[q][q]) / 2 * A[p][q]
    t = -alpha + sign(alpha) * math.sqrt(alpha * alpha + 1)
    c = 1 / math.sqrt(1 + t * t)
    s = t / math.sqrt(1 + t * t)
    return t, c, s


def recalculateMatrixA(A, n, p, q, t, c, s):
    B = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(0, n):
        if i != p and i != q:
            B[p][i] = c * A[p][i] + s * A[q][i]
            B[q][i] = -s * A[i][p] + c * A[q][i]
            B[i][q] = B[q][i]
            B[i][p] = B[p][i]
    B[p][p] = A[p][p] + t * A[p][q]
    B[q][q] = A[q][q] - t * A[p][q]
    B[p][q], B[q][p] = 0, 0
    return B


def recalculateU(U, p, q, c, s):
    V = [[0 for _ in range(len(U))] for _ in range(len(U))]
    for i in range(len(U)):
        V[i][p] = c * U[i][p] + s * U[i][q]
        V[i][q] = -s * U[i][p] + c * U[i][q]
    return V


def Jacobi(A, n):
    kmax = 1000
    eps = 10 ** -6
    k = 0
    U = np.identity(n)
    p, q = determineMaxIndex(A, n)
    t, c, s = determineTheta(A, p, q)
    while A[p][q] > eps and k <= kmax:
        A = recalculateMatrixA(A, n, p, q, t, c, s)
        U = recalculateU(U, p, q, c, s)
        p, q = determineMaxIndex(A, n)
        t, c, s = determineTheta(A, p, q)
        k += 1
    return A, U


if __name__ == '__main__':
    test = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    Afinal, Uf = Jacobi(test, len(test))
    print(test)
    print(Afinal)
    print(Uf)
