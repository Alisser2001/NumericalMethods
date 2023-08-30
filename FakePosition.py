import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import symbols
from sympy import lambdify
def fxr(xl, xu, yl, yu):
    return (xu - ((yu*(xl-xu))/(yl-yu)))

def getErr(xl, xu):
    return abs(xu - xl)

def FakePosition(f, xl, xu, stopCri, count):
        xr = fxr(xl, xu, f(xl), f(xu))
        err = getErr(xl, xu)
        print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format(count, xu, xl, xr, f(xu), f(xl), f(xr), round(err, 7)))
        if f(xl)*f(xr) == 0 or err < stopCri:
            return xr
        if f(xl)*f(xr) < 0:
            count += 1
            return FakePosition(f, xl, xr, stopCri, count)
        if f(xl)*f(xr) > 0:
            count += 1
            return FakePosition(f, xr, xu, stopCri, count)

def Solution():
    print("")
    x = symbols('x')
    fn = sympify(input('Ingresa la función: '))
    f = lambdify(x, fn)
    xl = float(input('Ingresa el valor menor de X: '))
    xu = float(input('Ingresa el valor mayor de X: '))
    stopCri = float(input('Ingresa el valor del críterio de tolerancia del error: '))
    count = 1
    print("")
    print("{:^60}".format("Método de la Bisección"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format("i", "xu", "xl", "xr", "f(xu)", "f(xl)", "f(xr)", "Error"))
    root = FakePosition(f, xl, xu, stopCri, count)
    print("Raíz: " + str(root))
    xpts = np.linspace(xl-10, xu+10)
    plt.plot(xpts, f(xpts))
    plt.title("Gráfica de la función " + str(fn))
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(root, 0, c="red")
    plt.scatter(xl, 0, c="blue")
    plt.scatter(xu, 0, c="blue")
    plt.annotate(round(root, 9), xy=(root, 0.5))
    plt.annotate(round(xl, 9), xy=(xl, 0.5))
    plt.annotate(round(xu, 9), xy=(xu, 0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()

Solution()

