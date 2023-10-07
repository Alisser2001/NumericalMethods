import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import symbols
from sympy import lambdify

def regla_simpson_1_3(f, fn, a, b):
    h = (b - a) / 2
    r = (h / 3) * (f(a) + 4 * f(a + h) + f(b))
    return r


def regla_simpson_3_8(f, fn, a, b):
    h = (b - a) / 3
    resultado = (3 * h / 8) * (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(b))
    return resultado

def Solution():
    print("")
    x = symbols('x')
    fn = sympify(input('Ingresa la función: '))
    f = lambdify(x, fn)
    xl = float(input('Ingresa el valor del límite inferior: '))
    xu = float(input('Ingresa el valor dle límite superior: '))
    print("")
    print("\nEl valor aprox. De la integral definida con Simpson 1/3 es: ", regla_simpson_1_3(f, fn, xl, xu))
    print("Para h = " + str(((xu - xl) / 2)) + " y f(x) = " + str(fn))
    print("Entre a = " + str(xl) + " y b = " + str(xu))
    print("")
    print("\nEl valor aprox. De la integral definida con Simpson 3/8 es: ", regla_simpson_3_8(f, fn, xl, xu))
    print("Para h = " + str(((xu - xl) / 3)) + " y f(x) = " + str(fn))
    print("Entre a = " + str(xl) + " y b = " + str(xu))
    plt.figure(figsize=(8, 6))
    xpts = np.linspace(xl - 10, xu + 10)
    ypts = f(xpts)
    plt.plot(xpts, ypts)
    plt.title("Gráfica de la función " + str(fn))
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(xl, f(xl), c="red")
    plt.scatter(xu, f(xu), c="red")
    plt.annotate((xl, f(xl)), xy=(xl, f(xl)))
    plt.annotate((xu, f(xu)), xy=(xu, f(xu)))
    plt.fill_between(xpts, ypts, where=[(x >= xl) and (x <= xu) for x in xpts], alpha=0.3, color='gray', label="Área")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.show()

Solution()