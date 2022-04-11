import sys
from copy import deepcopy

import numpy


def readFromFile(filepathA, filepathB, e):
    b, d, values, indexes, lineStart = [], [], [], [], []

    with open(filepathA) as fileA:
        n = int(fileA.readline())
        lastLine = -1
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
            values.append(x)
            indexes.append(j)
            if lastLine != i:
                lineStart.append(len(values) - 1)
                lastLine = i

    with open(filepathB) as fileB:
        for line in fileB:
            b.append(float(line))
    return values, indexes, lineStart, n, d, b


def solveJacobi(val, colI, lineS, n, d, b, e):
    kmax = 10000
    xc = [0 for _ in range(0, n)]
    k = 0
    while True:
        xp = deepcopy(xc)

        xc = deepcopy(b)
        line = 0
        for i in range(0, len(val)):
            if line < len(lineS) - 1 and i > lineS[line]:
                line += 1
            if line != colI[i]:
                xc[line] -= val[i] * xp[colI[i]]
                xc[colI[i]] -= val[i] * xp[line]
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


if __name__ == '__main__':
    eps = 10 ** -6
    values1, colIndexes1, lineStart1, n1, d1, b1 = readFromFile('inputs/a_1.txt', 'inputs/b_1.txt', eps)
    x1 = solveJacobi(values1, colIndexes1, lineStart1, n1, d1, b1, eps)
    for x in x1:
        print(f"{x} ----- {abs(x - 1)}")
