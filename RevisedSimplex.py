import numpy as np
import copy
from tabulate import tabulate

def getZCoefs(numVars):
    coefsZ = []
    for i in range(0, numVars):
        coef = float(input("Ingresa el valor del coeficiente de X" + str(i + 1) + " en Z: "))
        coefsZ.append(coef)
    return coefsZ

def getRestrictCoefs(numRest, numVars):
    coefsRest = []
    for i in range(0, numRest):
        for j in range(0, numVars):
            coef = float(
                input("Ingresa el valor del coeficiente de X" + str(j + 1) + " en la restricción " + str(i + 1) + ": "))
            coefsRest.append((i, "X" + str(j + 1), coef))
    return coefsRest

def getTypeRestric(numRest):
    typeRest = []
    slackVars = 0
    artVars = 0
    for i in range(0, numRest):
        t = input("Ingresa el tipo de la restriccición " + str(i + 1) + " (>=, ==, <=): ")
        if t == "<=" or t == ">=":
            slackVars += 1
        if t == "==":
            artVars += 1
        typeRest.append(t)
    return typeRest, slackVars, artVars

def getRightSide(numRest):
    right = []
    for i in range(0, numRest):
        val = float(input("Ingresa el valor al lado derecho de la restricción " + str(i + 1) + ": "))
        right.append([val])
    return right

def getZ(coefsZ):
    Z = ""
    for i in range(0, len(coefsZ)):
        Z = Z + "(" + str(coefsZ[i]) + ")" + "X" + str(i + 1) + (" + " if i < len(coefsZ) - 1 else "")
    return Z

def getRestrictions(numRest, coefsRest, numVars, typeRest, right):
    Rest = ["" for _ in range(numRest)]
    for i in range(0, len(coefsRest)):
        Rest[coefsRest[i][0]] = Rest[coefsRest[i][0]] + "(" + str(coefsRest[i][2]) + ")" + coefsRest[i][1] + (
            " + " if int(coefsRest[i][1][1]) < numVars else "")
    for i in range(0, len(Rest)):
        Rest[i] = Rest[i] + " " + typeRest[i] + " " + str(right[i][0])
    return Rest

def getEstandarZ(Z, slackVars, artVars):
    estZ = Z
    for i in range(0, slackVars+artVars):
        estZ = estZ + " + (0)" + "S" + str(i+1)
    return estZ

def getEstandarRestric(numRest, coefsRest, numVars, typeRest, right):
    estRest = ["" for _ in range(numRest)]
    for i in range(0, len(coefsRest)):
        estRest[coefsRest[i][0]] = estRest[coefsRest[i][0]] + "(" + str(coefsRest[i][2]) + ")" + coefsRest[i][1] + (
            " + " if int(coefsRest[i][1][1]) < numVars else "")
    for i in range(0, len(estRest)):
        if typeRest[i] == ">=":
            estRest[i] = estRest[i] + " - (1.0)S" + str(i + 1)
        if typeRest[i] == "<=" or typeRest[i] == "==":
            estRest[i] = estRest[i] + " + (1.0)S" + str(i + 1)
    for i in range(0, len(estRest)):
        estRest[i] = estRest[i] + " == " + str(right[i][0])
    return estRest

def printCanonModel(obj, Z, Rest):
    print("\nForma canócica del módelo: \n")
    print(obj + " Z = " + Z)
    for i in range(0, len(Rest)):
        print("Rest " + str(i + 1) + ": " + Rest[i])

def printEstandarModel(obj, estZ, estRest):
    print("\nForma estándar del módelo: \n")
    print(obj + " Z = " + estZ)
    for i in range(0, len(estRest)):
        print("Rest " + str(i + 1) + ": " + estRest[i])

def getXandR(numVars, slackVars, artVars):
    X = []
    R = []
    for i in range(0, numVars, artVars):
        X.append(["X" + str(i + 1)])
        R.append("X" + str(i + 1))
    for i in range(0, slackVars+artVars):
        R.append("S" + str(i + 1))
    return X, R

def getb(right):
    b = []
    for i in range(0, len(right)):
        b.append(right[i])
    return b

def getA(numRest, coefsRest):
    A = [[] for _ in range(0, numRest)]
    for i in range(0, len(coefsRest)):
        A[coefsRest[i][0]].append(coefsRest[i][2])
    return A

def getB(numRest, slackVars, typeRest, artVars):
    B = np.array([[0 for _ in range(0, slackVars+artVars)] for _ in range(0, numRest)])
    for i in range(0, numRest):
        if typeRest[i] == ">=":
            B[i][i] = -1
        if typeRest[i] == "<=" or typeRest[i] == "==":
            B[i][i] = 1
    return B

def printMatricialModel(C, b, X, A, R, Xs, B):
    print("\nC = \n", np.array(C))
    print("\nb = \n", np.array(b))
    print("\nX = \n", np.array(X))
    print("\nA = \n", np.array(A))
    print("\nXs = \n", np.array(Xs))
    print("\nB = \n", np.array(B))
    print("\n", np.array(R), ">= 0\n")

def printIteration(ops):
    thisOps = copy.deepcopy(ops)
    for i in range(0, len(thisOps)):
        for j in range(0, len(thisOps[i])):
            thisOps[i][j] = str(thisOps[i][j])
    print("Z = ", thisOps[0][3])
    print("\n", tabulate(thisOps, headers=["Columna 1", "Columna 2", "Columna 3", "Columna 4"], tablefmt="grid"))

def Solution():
    print("\nCada variable, sea de holgura, exceso o artificial se añadirá a la ecuación con el prefijo S")
    print("En el mismo orden que aparecen en las restricciones.\n")
    numVars = int(input("Ingrese la cantidad de variables de decisión del problema: "))
    numRest = int(input("Ingrese la cantidad de restricciones del problema: "))
    obj = input("¿Cuál es el objetivo de la función (Max - Min)?: ")
    coefsZ = getZCoefs(numVars)
    coefsRest = getRestrictCoefs(numRest, numVars)
    typeRest, slackVars, artVars = getTypeRestric(numRest)
    right = getRightSide(numRest)
    Z = getZ(coefsZ)
    Rest = getRestrictions(numRest, coefsRest, numVars, typeRest, right)
    # Imprimimos la forma canónica del módelo
    printCanonModel(obj, Z, Rest)
    estZ = getEstandarZ(Z, slackVars, artVars)
    estRest = getEstandarRestric(numRest, coefsRest, numVars, typeRest, right)
    # Imprimimos la forma estándar del módelo
    printEstandarModel(obj, estZ, estRest)
    # Empezamos a formar el módelo matricial
    C = coefsZ
    X, R = getXandR(numVars, slackVars, artVars)
    b = getb(right)
    A = getA(numRest, coefsRest)
    Xs = [["S" + str(i + 1)] for i in range(0, numRest)]
    B = np.array(getB(numRest, slackVars, typeRest, artVars))
    # Imprimimos nuestro modelo matricial aumentado
    printMatricialModel(C, b, X, A, R, Xs, B)
    iterations(Aj=A, B=B, b=b, Cb=np.array([0 for _ in range(0, slackVars+artVars)]), Cj=C, numVars=numVars, artVars=artVars, slackVars=slackVars, numRest=numRest, obj=obj)


def iterations(Aj, B, b, Cb, Cj, numVars, slackVars, numRest, obj, artVars, j=0):
    Aj = np.array(Aj)
    B = np.array(B)
    b = np.array(b)
    Cb = np.array(Cb)
    Cj = np.array(Cj)
    if obj == "Min" or obj == "min":
        Cj = (-1)*Cj
    Xj = ["X"+str(i+1) for i in range(0, numVars)]
    Xb = ["S"+str(i+1) for i in range(0, slackVars+artVars)]
    Zeros = np.array([[0] for _ in range(0, numRest)])
    ops = [[0, 0, 0, 0], [0, 0, 0, 0]]
    ops[0][0] = np.array([1])
    ops[1][0] = Zeros
    condition = True
    ops[0][1] = np.dot(np.dot(Cb, np.linalg.inv(B)), Aj) - Cj
    it = 0
    while condition:
        if np.linalg.det(B) == 0:
            print("El determinate de B es cero y no se puede seguir calculando su inversa.")
            return
        ops[0][1] = np.dot(np.dot(Cb, np.linalg.inv(B)), Aj) - Cj
        ops[0][2] = np.dot(Cb, np.linalg.inv(B))
        ops[0][3] = np.dot(np.dot(Cb, np.linalg.inv(B)), b)
        ops[1][1] = np.dot(np.linalg.inv(B), Aj)
        ops[1][2] = np.linalg.inv(B)
        ops[1][3] = np.dot(np.linalg.inv(B), b)
        printIteration(ops)
        condition = False
        if obj == "Max" or obj == "max":
            elements = ops[0][1].tolist()
            for e in elements:
                e = float(e)
                if e <= 0:
                    condition = True
        if obj == "Min" or obj == "min":
            elements = ops[0][1].tolist()
            for e in elements:
                e = float(e)
                if e >= 0:
                    condition = True
        if condition == False: break
        j = np.argmin(np.dot(np.dot(Cb, np.linalg.inv(B)), Aj) - Cj) if obj=="Max" or obj=="max" else np.argmax(np.dot(np.dot(Cb, np.linalg.inv(B)), Aj) - Cj)
        pivot = []
        for i in range(0, len(Aj[:, j])):
                k = [Aj[:, j][i]]
                pivot.append(k)
        div_result = np.where(np.dot(np.linalg.inv(B), np.array(pivot)) > 0, np.dot(np.linalg.inv(B), b) / np.dot(np.linalg.inv(B), np.array(pivot)), np.inf)
        outElement = np.argmin(div_result)
        print("Iteration:", it+1)
        print("In: ", Xj[j])
        print("Out: ", Xb[outElement])
        Xbpivot = Xb[outElement]
        Xjpivot = Xj[j]
        Xj[j] = Xbpivot
        Xb[outElement] = Xjpivot
        print("Xj =", Xj)
        print("Xb =", Xb)
        Cbpivot = Cb[outElement]
        Cjpivot = Cj[j]
        Cj[j] = Cbpivot
        Cb[outElement] = Cjpivot
        p1 = []
        p2 = []
        for i in range(0, len(Aj[:, j])):
            k = [Aj[:, j][i]]
            p1.append(k)
        for i in range(0, len(B[:, outElement])):
            k = [B[:, outElement][i]]
            p2.append(k)
        p1 = np.array(p1)
        p2 = np.array(p2)
        for i in range(0, len(Aj)):
            Aj[i][j] = p2[i][0]
        for i in range(0, len(B)):
            B[i][outElement] = p1[i][0]
        it += 1
    for i in range(0, len(Xb)):
        print(Xb[i], "=", ops[1][3][i][0])
    for i in range(0, len(Xj)):
        print(Xj[i], "=", 0)
    print(obj, "Z = ", (ops[0][3][0] if obj=="Max" or obj=="max" else (-1)*ops[0][3][0]))

Solution()