import numpy as np
import plotly.graph_objects as go
import coef


def get_u():
    u = 1 / 10
    while 1.0 + u != 1.0:
        u /= 10
    # At this point, 1.0 + u == 1.0, so go back one step
    return u * 10


def numere_adunate_non_asociative():
    u = get_u()
    a = 1.0
    b = u / 10
    c = u / 10
    return a, b, c


def numere_inmultite_non_asociative():
    return 0.1, 0.2, 0.3


# sin(pi/4 * x)
def sin_aprox(value):
    value /= (np.pi / 4)
    a, b = coef.sin_coef()
    squared = value * value
    P = a[0] + squared * (a[1] + squared * (a[2] + squared * (a[3] + squared * a[4])))
    Q = b[0] + squared * (b[1] + squared * (b[2] + squared * (b[3] + squared * b[4])))
    return value * (P / Q)


def cos_aprox(value):
    value /= np.pi / 4
    a, b = coef.cos_coef()
    value *= value
    P = a[0] + value * (a[1] + value * (a[2] + value * (a[3] + value * a[4])))
    Q = b[0] + value * (b[1] + value * (b[2] + value * (b[3] + value * b[4])))
    return P / Q


def ln_aprox(value):
    a, b = coef.ln_coef()
    z = (value - 1) / (value + 1)
    result = z
    z *= z
    P = a[0] + z * (a[1] + z * (a[2] + z * (a[3] + z * a[4])))
    Q = b[0] + z * (b[1] + z * (b[2] + z * (b[3] + z * b[4])))
    return result * (P / Q)


def ex1():
    print("Ex1:")
    print(f"Precizia masina este {get_u()}")


def ex2():
    print("Ex2:")
    a, b, c = numere_adunate_non_asociative()
    print(f"(a + b) + c = {(a + b) + c}\na + (b + c) = {a + (b + c)}")
    a, b, c = numere_inmultite_non_asociative()
    print(f"(a * b) * c = {(a * b) * c}\na * (b * c) = {a * (b * c)}")


def sinGraph():
    x = np.linspace(-10, 10, 10000)
    y = [sin_aprox(value) for value in x]
    fig = go.Figure(data=go.Scatter(x=x, y=y, name="approximation"))
    y = [np.sin(value) for value in x]
    fig.add_trace(go.Scatter(x=x, y=y, name="numpy"))
    fig.show()


def cosGraph():
    x = np.linspace(-10, 10, 10000)
    y = [cos_aprox(value) for value in x]
    fig = go.Figure(data=go.Scatter(x=x, y=y, name="approximation"))
    y = [np.cos(value) for value in x]
    fig.add_trace(go.Scatter(x=x, y=y, name="numpy"))
    fig.show()


def lnGraph():
    x = np.linspace(0.01, 100, 1000)
    y = [ln_aprox(value) for value in x]
    fig = go.Figure(data=go.Scatter(x=x, y=y, name="approximation"))
    y = [np.log(value) for value in x]
    fig.add_trace(go.Scatter(x=x, y=y, name="numpy"))
    fig.show()


def ex3():
    print("Ex3:")
    print("Commands: gsin, gcos, gln, exit")
    while True:
        command = input()
        if command == "gsin":
            sinGraph()
        if command == "gcos":
            cosGraph()
        if command == "gln":
            lnGraph()
        if command == "exit":
            break

if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
