import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import symbols
from sympy import lambdify

def fd(xl, xu):
    phi = (1 / round((1 + np.sqrt(5)) / 2, 7))
    return phi*(xu - xl)

def fx1(d, xl):
    return xl + d

def fx2(d, xu):
    return xu - d

def getErr(x1, x2):
    return abs(x2 - x1)

def GoldenReason(f, xl, xu, stopCri, count, errList):
    d = fd(xl, xu)
    x1 = fx1(d, xl)
    x2 = fx2(d, xu)
    err = getErr(x1, x2)
    errList.append(err)
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format(count, xu, xl, d, x1, x2, f(xu), f(xl), f(x1), f(x2), round(err, 7)))
    if f(x2) == f(x1) or err < stopCri or count > 900:
        return [x1, f(x1)], errList, count
    if f(x2) > f(x1):
        count += 1
        return GoldenReason(f, xl, x1, stopCri, count, errList)
    if f(x2) < f(x1):
        count += 1
        return GoldenReason(f, x2, xu, stopCri, count, errList)

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
    print("{:^60}".format("Método de la Razón Dorada"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format("i", "xu", "xl", "d", "x1", "x2", "f(xu)", "f(xl)", "f(x1)", "f(x2)", "Error"))

    # Grafica del error
    plt.figure(figsize=(8, 6))
    plt.title("Gráfica del Error")
    plt.axhline(color="black")
    plt.axvline(color="black")
    errlist = []

    max, err_list, c = GoldenReason(f, xl, xu, stopCri, count, errlist)
    print("\nMáximo: " + str(max[1]))

    plt.plot(range(0, c), err_list, c="red")
    plt.xlabel("x")
    plt.ylabel("Error: abs(x2-x1)")
    plt.grid(True, which='both')
    plt.show()

    #Grafica de la función
    plt.figure(figsize=(8, 6))
    xpts = np.linspace(xl-10, xu+10)
    plt.plot(xpts, f(xpts))
    plt.title("Gráfica de la función " + str(fn))
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(max[0], max[1], c="red")
    plt.scatter(xl, 0, c="blue")
    plt.scatter(xu, 0, c="blue")
    plt.annotate(round(max[1], 9), xy=(max[0], max[1]))
    plt.annotate(round(xl, 9), xy=(xl, 0.5))
    plt.annotate(round(xu, 9), xy=(xu, 0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()

Solution()
