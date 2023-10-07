import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import symbols
from sympy import lambdify

def Trapeze(f, fn, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(0, n):
        xi = a + i * h
        xi1 = a + (i + 1) * h
        area = (f(xi) + f(xi1)) * h / 2
        s += area
        print("{:^30} {:^30} {:^30} {:^30}".format(str(i+1), str(xi), str(xi1), str(s)))
    return s

def Solution():
    print("")
    x = symbols('x')
    fn = sympify(input('Ingresa la función: '))
    f = lambdify(x, fn)
    xl = float(input('Ingresa el valor del límite inferior: '))
    xu = float(input('Ingresa el valor dle límite superior: '))
    n = int(input('Ingresa el valor de los sub-intervalos: '))
    print("")
    print("{:^120}".format("Método del Trapecio Compuesto"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30}".format("i", "Xi", "Xi+1", "Area Total"))
    print("")
    print("\nEl valor aprox. De la integral definida es: ", Trapeze(f, fn, xl, xu, n))
    print("Para h = " + str(((xu-xl)/n)) + " y f(x) = " + str(fn))
    print("Entre a = " + str(xl) + " y b = " + str(xu))
    print("Tomando " + str(n) + " sub-intervalos.")
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