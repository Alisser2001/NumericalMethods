import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import diff
from sympy import symbols
from sympy import lambdify
import random

def RandomSearch(f, xl, xu, yl, yu, n, maxf):
    for j in range(1, n):
        r = random.random()
        x = xl + (xu - xl)*r
        y = yl + (yu - yl)*r
        fn = f(x, y)
        print("{:^30} {:^30} {:^30} {:^30}".format(j, x, y, fn))
        if fn > maxf:
            maxf = fn
    return maxf


def Solution():
    print("")
    x = symbols('x')
    y = symbols('y')
    count = 1
    maxf = -1E9
    fn = sympify(input('Ingresa la función: '))
    f = lambdify((x, y), fn)
    xl = float(input("Ingresa el valor de xl: "))
    xu = float(input("Ingresa el valor de xu: "))
    yl = float(input("Ingresa el valor de yl: "))
    yu = float(input("Ingresa el valor de yu: "))
    n = int(input("Ingrese el número de iteraciones: "))
    print("")
    print("{:^60}".format("Método de Búsqueda Aleatoria"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30}".format("i", "x", "y", "f(x, y)"))
    maxFinal = RandomSearch(f, xl, xu, yl, yu, n, maxf)
    print("\nMáximo en Z = " + str(maxFinal))
    xpts = np.linspace(xl - 10, xu + 10, 50)
    ypts = np.linspace(yl - 10, xu + 10, 50)
    X, Y = np.meshgrid(xpts, ypts)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, f(X, Y), cmap='viridis')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    plt.title("Gráfica de la función " + str(fn))
    plt.show()

Solution()