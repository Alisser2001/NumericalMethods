import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import diff
from sympy import symbols
from sympy import lambdify

def getError(x0, x1):
    return abs(x1-x0)

def getRoot(f, fd, x0, stopCri, count, errlistRoot):
    xa = x0
    xs = xa - (f(xa) / fd(xa))
    err = getError(xa, xs)
    errlistRoot.append(err)
    print("{:^30} {:^30} {:^30} {:^30} {:^30}".format(count, xa, f(xa), fd(xa), err))
    if f(xs) != 0 and err > stopCri and not count > 900:
        count += 1
        return getRoot(f, fd, xs, stopCri, count, errlistRoot)
    return xs, errlistRoot, count

def getMinOrMax(f, fd, fdd, x0, stopCri, count, errlistMax):
    xa = x0
    xs = xa - (fd(xa) / fdd(xa))
    err = getError(xa, xs)
    errlistMax.append(err)
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format(count, xa, f(xa), fd(xa), fdd(xa), err))
    if err > stopCri and not count > 900:
        count += 1
        return getMinOrMax(f, fd, fdd, xs, stopCri, count, errlistMax)
    return xs, f(xs), errlistMax, count

def NewtonMethod(f, fd, fdd, x0, stopCri, count):
    print("")
    print("{:^60}".format("Método de Newton Para la Raíz"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30} {:^30}".format("i", "x", "f(x)", "f'(x)", "Error"))

    # Grafica del error de la raiz
    plt.figure(figsize=(8, 6))
    plt.title("Gráfica del Error para la Raíz")
    plt.axhline(color="black")
    plt.axvline(color="black")
    errlistRoot = []

    root, err_list_root, cr = getRoot(f, fd, x0, stopCri, count, errlistRoot)

    plt.plot(range(0, cr), err_list_root, c="red")
    plt.xlabel("x")
    plt.ylabel("Error: abs(x1-x0)")
    plt.grid(True, which='both')
    plt.show()

    print("\n")
    print("{:^60}".format("Método de Newton Para Mín o Máx"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format("i", "x", "f(x)", "f'(x)", "f''(x)", "Error"))

    # Grafica del error para el máximo
    plt.figure(figsize=(8, 6))
    plt.title("Gráfica del Error para el máximo o mínimo")
    plt.axhline(color="black")
    plt.axvline(color="black")
    errlistMax = []

    xs, ys, err_list_max, cm = getMinOrMax(f, fd, fdd, x0, stopCri, count, errlistMax)

    plt.plot(range(0, cm), err_list_max, c="red")
    plt.xlabel("x")
    plt.ylabel("Error: abs(x1-x0)")
    plt.grid(True, which='both')
    plt.show()

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
    plt.figure(figsize=(8, 6))
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
