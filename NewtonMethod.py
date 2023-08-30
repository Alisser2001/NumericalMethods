import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import diff
from sympy import symbols
from sympy import lambdify

def getError(x0, x1):
    return np.abs(x1-x0)

def getRoot(f, fd, x0, stopCri, count):
    xa = x0
    xs = xa - (f(xa) / fd(xa))
    err = getError(xa, xs)
    print("{:^30} {:^30} {:^30} {:^30} {:^30}".format(count, xa, f(xa), fd(xa), err))
    if f(xs) != 0 and err > stopCri:
        count += 1
        return getRoot(f, fd, xs, stopCri, count)
    return xs

def getMinOrMax(f, fd, fdd, x0, stopCri, count):
    xa = x0
    xs = xa - (fd(xa) / fdd(xa))
    err = getError(xa, xs)
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format(count, xa, f(xa), fd(xa), fdd(xa), err))
    if err > stopCri:
        count += 1
        return getMinOrMax(f, fd, fdd, xs, stopCri, count)
    return xs, f(xs)

def NewtonMethod(f, fd, fdd, x0, stopCri, count):
    print("")
    print("{:^60}".format("Método de Newton Para la Raíz"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30} {:^30}".format("i", "x", "f(x)", "f'(x)", "Error"))
    root = getRoot(f, fd, x0, stopCri, count)
    print("\n")
    print("{:^60}".format("Método de Newton Para Mín o Máx"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format("i", "x", "f(x)", "f'(x)", "f''(x)", "Error"))
    xs, ys = getMinOrMax(f, fd, fdd, x0, stopCri, count)
    return root, xs, ys

def Solution():
    print("")
    x = symbols('x')
    count = 1
    fn = sympify(input('Ingresa la función: '))
    f = lambdify(x, fn)
    fnd = diff(fn, x, 1)
    fd = lambdify(x, fnd)
    fndd = diff(fn, x, 2)
    fdd = lambdify(x, fndd)
    x0 = float(input("Ingresa el valor de X0: "))
    stopCri = float(input("Ingrese el criterio de parada del error: "))
    root, xs, ys = NewtonMethod(f, fd, fdd, x0, stopCri, count)
    result = "Mínimo" if fdd(xs) > 0 else "Máximo"
    print("\nRaíz en X = " + str(root))
    print(result + " en: " + "(" + str(xs) + ", " + str(ys) + ")")
    xl = xs if xs < root else root
    xu = xs if xs > root else root
    xpts = np.linspace(xl - 10, xu + 10)
    plt.plot(xpts, f(xpts))
    plt.title("Gráfica de la función " + str(fn))
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(root, 0, c="red")
    plt.scatter(xs, ys, c="blue")
    plt.annotate(round(root, 9), xy=(root, 0.5))
    plt.annotate((round(xs, 9), round(ys, 9)), xy=(xs, ys + 0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()

Solution()