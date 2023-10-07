import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from tabulate import tabulate
from sympy import lambdify

def FirstDifferences(pts):
    sD = []
    for i in range(0, len(pts)-1):
        value = (pts[i+1][1] - pts[i][1]) / (pts[i+1][0] - pts[i][0])
        sD.append(("X"+str(i+1)+", X"+str(i+2), value))
    return sD

def GetDifferences(pts, bD, grade):
    aD = []
    for i in range(0, len(bD)-1):
        value = (bD[i+1][1] - bD[i][1]) / (pts[i+grade][0] - pts[i][0])
        val = ""
        for j in range(0, grade+1):
            val = val + "X" + str(i+j+1) + (", " if j<grade else "")
        aD.append((val, value))
    return aD

def Solution():
    print("")
    numPts = int(input("Ingrese la cantidad de puntos a evaluar: "))
    pts = []
    for i in range(0, numPts):
        x = float(input("Ingrese el valor de X" + str(i+1) + ": "))
        y = float(input("Ingrese el valor de Y" + str(i+1) + ": "))
        pts.append((x, y))
    ops = []
    ops.append(FirstDifferences(pts))
    for i in range(1, numPts-1):
        ops.append(GetDifferences(pts, ops[i-1], i+1))
    data = []
    for i in range(0, len(ops)):
        for j in range(0, len(ops[i])):
            data.append([ops[i][j][0], ops[i][j][1]])
        print("\n", tabulate(data, headers=["Operación", "Valor"], tablefmt="grid"))
        data = []
    coefPolPr = []
    coefPolRe = []
    varPolP = []
    varPolR = []
    for i in range(0, len(pts)-1):
        varPolP.append("(x - "+str(pts[i][0])+")")
        varPolR.append("(x - "+str(pts[-1-i][0])+")")
    coefPolPr.append(pts[0][1])
    coefPolRe.append(pts[-1][1])
    for i in range(0, len(ops)):
        coefPolPr.append(ops[i][0][1])
        coefPolRe.append(ops[i][-1][1])
    Pp = ""
    Pr = ""
    for i in range(0, len(coefPolPr)):
        varsPr = ""
        varsRe = ""
        for j in range(0, i):
            varsPr = varsPr + "*" + varPolP[j]
            varsRe = varsRe + "*" + varPolR[j]
        Pp = Pp + "(" + str(coefPolPr[i]) + ")" + varsPr + (" + " if i < len(coefPolPr) - 1 else "")
        Pr = Pr + "(" + str(coefPolRe[i]) + ")" + varsRe + (" + " if i < len(coefPolRe) - 1 else "")
    print("\nProgressive P(x) = " + str(Pp))
    print("\nRegressive P(x) = " + str(Pr))
    x = symbols('x')
    fp = lambdify(x, str(Pp))
    fr = lambdify(x, str(Pr))
    #Gráfica del polinomio progesivo
    plt.figure(figsize=(8, 6))
    xpts = np.linspace(pts[0][0] - 10, pts[-1][0] + 10)
    plt.plot(xpts, fp(xpts))
    plt.title("Gráfica del polinomio progresivo P(x) = " + str(Pp))
    plt.axhline(color="black")
    plt.axvline(color="black")
    for i in range(0, len(pts)):
        plt.scatter(pts[i][0], pts[i][1], c="red")
        plt.annotate(pts[i], xy=(pts[i][0], pts[i][1]))
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.grid(True, which='both')
    plt.show()
    # Gráfica del polinomio regresivo
    plt.figure(figsize=(8, 6))
    xpts = np.linspace(pts[0][0] - 10, pts[-1][0] + 10)
    plt.plot(xpts, fr(xpts))
    plt.title("Gráfica del polinomio regresivo P(x) = " + str(Pr))
    plt.axhline(color="black")
    plt.axvline(color="black")
    for i in range(0, len(pts)):
        plt.scatter(pts[i][0], pts[i][1], c="red")
        plt.annotate(pts[i], xy=(pts[i][0], pts[i][1]))
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.grid(True, which='both')
    plt.show()
Solution()