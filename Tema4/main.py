import sys
from copy import deepcopy
import time

import numpy.linalg


def readFromFile(filepath_a1, filepath_b1, e):
    b, d = [], []
    with open(filepath_a1) as fileA:
        n = int(fileA.readline())
        a = [{} for _ in range(0, n)]

        for line in fileA:
            if line == '\n':
                continue

            x, i, j = line.split(',')
            x, i, j = float(x), int(i), int(j)
            if i == j:
                d.append(x)
                if abs(x) <= e:
                    print(f'elementul de pe diagonala de pe linia {i}'
                          f' este nul deci nu se poate rezolva sistemul cu metoda Jacobi')
                    sys.exit()
            a[i][j] = x

    with open(filepath_b1) as fileB:
        for line in fileB:
            b.append(float(line))

    for i in range(0, n):
        a[i] = dict(sorted(a[i].items()))
    return a, n, b, d


def solveJacobi(a, b, d, n, e):
    kmax = 10000
    xc = [0 for _ in range(0, n)]
    k = 0
    while True:
        xp = deepcopy(xc)

        xc = deepcopy(b)
        for i in range(0, n):
            for key in a[i].keys():
                if i != key:
                    xc[i] -= a[i][key] * xp[key]
                    xc[key] -= a[i][key] * xp[i]
        for i in range(0, n):
            xc[i] /= d[i]

        deltax = numpy.linalg.norm(numpy.subtract(xc, xp))

        if deltax < e:
            print(f'algorithm converges, did {k} iterations')
            return xc

        k += 1
        if k > kmax or deltax > 10 ** 8:
            print('algorithm diverges')
            return


def multiplication(a, n, x):
    result = [0 for _ in range(0, n)]
    for i in range(0, n):
        for key in a[i].keys():
            result[i] += a[i][key] * x[key]
            if i != key:
                result[key] += a[i][key] * x[i]
    return result

if __name__ == '__main__':
    eps = 10 ** -6
    A1, nA1, B1, D1 = readFromFile('inputs/a_1.txt', 'inputs/b_1.txt', eps)
    A2, nA2, B2, D2 = readFromFile('inputs/a_2.txt', 'inputs/b_2.txt', eps)
    A3, nA3, B3, D3 = readFromFile('inputs/a_3.txt', 'inputs/b_3.txt', eps)
    A4, nA4, B4, D4 = readFromFile('inputs/a_4.txt', 'inputs/b_4.txt', eps)
    A5, nA5, B5, D5 = readFromFile('inputs/a_5.txt', 'inputs/b_5.txt', eps)
    start_time = time.time()
    x1 = solveJacobi(A1, B1, D1, nA1, eps)
    if x1:
        print(f'First norm {numpy.linalg.norm(numpy.subtract(multiplication(A1, nA1, x1), B1))}')
    print("A1 --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    x2 = solveJacobi(A2, B2, D2, nA2, eps)
    if x2:
        print(f'Second norm {numpy.linalg.norm(numpy.subtract(multiplication(A2, nA2, x2), B2))}')
    print("A2 --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    x3 = solveJacobi(A3, B3, D3, nA3, eps)
    if x3:
        print(f'Third norm {numpy.linalg.norm(numpy.subtract(multiplication(A3, nA3, x3), B3))}')
    print("A3 --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    x4 = solveJacobi(A4, B4, D4, nA4, eps)
    if x4:
        print(f'Fourth norm {numpy.linalg.norm(numpy.subtract(multiplication(A4, nA4, x4), B4))}')
    print("A4 --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    x5 = solveJacobi(A5, B5, D5, nA5, eps)
    if x5:
        print(f'Fifth norm {numpy.linalg.norm(numpy.subtract(multiplication(A5, nA5, x5), B5))}')
    print("A5 --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
