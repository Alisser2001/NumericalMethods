import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import symbols
from sympy import lambdify

def TwoPoints(x0, h, f):
    return (f(x0 + h) - f(x0)) / h

def ThreePoints(x0, h, f):
    return (f(x0 + h) - f(x0 - h)) / (2*h)

def FivePoints(x0, h, f):
    return (f(x0 - (2*h)) - (8*f(x0 - h)) + (8*f(x0 + h)) - f(x0 + (2*h))) / (12*h)

def SolveTwoPoints(f, x0, h):
    print("")
    print("{:^120}".format("Valor estimado con dos puntos y x0 = " + str(x0)))
    print("")
    print("{:^60} {:^60}".format("h", "[f(x0+h)-f(x0)]/h"))
    xp = 0
    while h > 1e-8:
        xp = TwoPoints(x0, h, f)
        print("{:^60} {:^60}".format(h, xp))
        h = h / 10
    return xp

def SolveThreePoints(f, x0, h):
    print("")
    print("{:^120}".format("Valor estimado con tres puntos y x0 = " + str(x0)))
    print("")
    print("{:^60} {:^60}".format("h", "[f(x0+h)-f(x0-h)]/2h"))
    xp = 0
    while h > 1e-8:
        xp = ThreePoints(x0, h, f)
        print("{:^60} {:^60}".format(h, xp))
        h = h / 10
    return xp

def SolveFivePoints(f, x0, h):
    print("")
    print("{:^120}".format("Valor estimado con cinco puntos y x0 = " + str(x0)))
    print("")
    print("{:^60} {:^60}".format("h", "[f(x0-2h)-8f(x0-h)+8f(x0+h)-f(x0+2h)]/12h"))
    xp = 0
    while h > 1e-8:
        xp = FivePoints(x0, h, f)
        print("{:^60} {:^60}".format(h, xp))
        h = h / 10
    return xp

def Solution():
    print("")
    x = symbols('x')
    fn = sympify(input('Ingresa la función: '))
    f = lambdify(x, fn)
    x0 = float(input("Ingresa el valor de X0: "))
    h = 0.1
    twoP = SolveTwoPoints(f, x0, h)
    threeP = SolveThreePoints(f, x0, h)
    fiveP = SolveFivePoints(f, x0, h)
    bestValue = max(twoP, threeP, fiveP)
    print("")
    print("Derivada igual a " + str(bestValue) + " en X = " + str(x0))
    plt.figure(figsize=(8, 6))
    xpts = np.linspace(x0 - 10, x0 + 10)
    plt.plot(xpts, f(xpts))
    plt.title("Gráfica de la función " + str(fn))
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(x0, f(x0), c="red")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()

Solution()