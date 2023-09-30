import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import symbols
from sympy import lambdify

def getErr(x1, x3):
    return abs(x1 - x3)

def x3Num(y0, y1, y2, x0, x1, x2):
    return (y0 * (x1 ** 2 - x2 ** 2) + y1 * (x2 ** 2 - x0 ** 2) + y2 * (x0 ** 2 - x1 ** 2))

def x3Den(y0, y1, y2, x0, x1, x2):
    return (2 * y0 * (x1 - x2) + 2 * y1 * (x2 - x0) + 2 * y2 * (x0 - x1))

def fx3(y0, y1, y2, x0, x1, x2):
    return (x3Num(y0, y1, y2, x0, x1, x2)/x3Den(y0, y1, y2, x0, x1, x2))

def CuadraticInterpolation(f, x0, x1, x2, stopCri, count, errList):
    y0 = f(x0)
    y1 = f(x1)
    y2 = f(x2)
    x3 = fx3(y0, y1, y2, x0, x1, x2)
    y3 = f(x3)
    err = getErr(x1, x3)
    errList.append(err)
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format(count, x0, x1, x2, x3, y0, y1, y2, y3, err))
    if y3 == y1 or err < stopCri or count > 900:
        return [x3, y3], errList, count
    if y3 > y1:
        count += 1
        return CuadraticInterpolation(f, x1, x3, x2, stopCri, count, errList)
    if y3 < y1:
        count += 1
        return CuadraticInterpolation(f, x0, x3, x1, stopCri, count, errList)

def Solution():
    print("")
    x = symbols('x')
    fn = sympify(input('Ingresa la función: '))
    f = lambdify(x, fn)
    x0 = float(input('Ingresa el valor menor de X: '))
    x1 = float(input('Ingresa el valor medio de X: '))
    x2 = float(input('Ingresa el valor mayor de X: '))
    stopCri = float(input('Ingresa el valor del críterio de tolerancia del error: '))
    count = 1
    print("")
    print("{:^60}".format("Método de la Interpolación Cuadrática"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format("i", "x0", "x1", "x2", "x3", "f(x0)", "f(x1)", "f(x2)", "f(x3)", "Error"))

    # Grafica del error
    plt.figure(figsize=(8, 6))
    plt.title("Gráfica del Error")
    plt.axhline(color="black")
    plt.axvline(color="black")
    errlist = []

    max, err_list, c = CuadraticInterpolation(f, x0, x1, x2, stopCri, count, errlist)
    print("\nMáximo: " + str(max[1]))

    plt.plot(range(0, c), err_list, c="red")
    plt.xlabel("x")
    plt.ylabel("Error: abs(x1-x3)")
    plt.grid(True, which='both')
    plt.show()

    #Grafica de la función
    plt.figure(figsize=(8, 6))
    xpts = np.linspace(x0-10, x2+10)
    plt.plot(xpts, f(xpts))
    plt.title("Gráfica de la función " + str(fn))
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(max[0], max[1], c="red")
    plt.scatter(x0, 0, c="blue")
    plt.scatter(x1, 0, c="blue")
    plt.scatter(x2, 0, c="blue")
    plt.annotate(round(max[1], 9), xy=(max[0], max[1]))
    plt.annotate(round(x0, 9), xy=(x0, 0.5))
    plt.annotate(round(x1, 9), xy=(x1, 0.5))
    plt.annotate(round(x2, 9), xy=(x2, 0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()

Solution()