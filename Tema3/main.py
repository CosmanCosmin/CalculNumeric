from copy import deepcopy


def readFromFile(fileName):
    with open(fileName) as file:
        n = int(file.readline())
        M = [{} for _ in range(0, n)]

        lines = file.readlines()
        for line in lines[1:]:
            if line.strip() == "":
                continue
            values = line.split(',')
            value, line, column = float(values[0]), int(values[1]), int(values[2])
            M[line][column] = value
    for i in range(0, n):
        M[i] = dict(sorted(M[i].items()))
    return n, M


def economicSum(a, b, n):
    result = deepcopy(a)
    for i in range(0, n):
        for key in b[i].keys():
            if key in result[i].keys():
                result[i][key] += b[i][key]
            else:
                result[i][key] = b[i][key]
        result[i] = dict(sorted(result[i].items()))
    return result


def economicProduct(a, n):
    result = [{} for _ in range(0, n)]
    for i in range(0, n):
        for j in range(0, i + 1):
            val = 0
            for k in range(0, n):
                if k <= i:
                    if k >= j:
                        if k in a[i] and j in a[k]:
                            val += a[i][k] * a[k][j]
                    else:
                        if k in a[i] and k in a[j]:
                            val += a[i][k] * a[j][k]
                else:
                    if j in a[k] and i in a[k]:
                        val += a[k][i] * a[k][j]
            if val != 0:
                result[i][j] = val
    for i in range(0, len(result)):
        result[i] = dict(sorted(result[i].items()))
    return result


def checkEqual(a, b):
    line = 0
    eps = 10 ** -6
    for lineA, lineB in zip(a, b):
        if lineA.keys() != lineB.keys():
            print(lineA, lineB, f"line = {line}", sep="\n")
            return False
        for key in lineA.keys():
            if abs(lineA[key] - lineB[key]) >= eps:
                print(lineA, lineB, f"line = {line}", sep="\n")
                return False
        line += 1
    return True


if __name__ == '__main__':
    nA, A = readFromFile("inputs/a.txt")
    nB, B = readFromFile("inputs/b.txt")
    nAplusB, AplusB = readFromFile("inputs/a_plus_b.txt")
    nAoriA, AoriA = readFromFile("inputs/a_ori_a.txt")
    print("The sums are" + ("" if checkEqual(economicSum(A, B, nA), AplusB) else " not") + " equal")
    print("The products are" + ("" if checkEqual(economicProduct(A, nA), AoriA) else " not") + " equal")
