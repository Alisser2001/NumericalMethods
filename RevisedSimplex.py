import numpy as np
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
    for i in range(0, numRest):
        t = input("Ingresa el tipo de la restriccición " + str(i + 1) + " (>=, ==, <=): ")
        if t == "<=" or t == ">=":
            slackVars += 1
        typeRest.append(t)
    return typeRest, slackVars

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

def getEstandarZ(Z, slackVars):
    estZ = Z
    for i in range(0, slackVars):
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
        if typeRest[i] == "<=":
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

def getXandR(numVars, slackVars):
    X = []
    R = []
    for i in range(0, numVars):
        X.append(["X" + str(i + 1)])
        R.append("X" + str(i + 1))
    for i in range(0, slackVars):
        R.append("S" + str(i + 1))
    return X, R

def getb(right):
    b = []
    for i in range(0, len(right)):
        b.append(right[i])
    return b

def getA(numRest, coefsRest, slackVars, typeRest):
    A = [[] for _ in range(0, numRest)]
    for i in range(0, len(coefsRest)):
        A[coefsRest[i][0]].append(coefsRest[i][2])
    return A

def getB(numRest, slackVars, typeRest):
    B = [[] for _ in range(0, numRest)]
    for i in range(0, numRest):
        s = [0 for _ in range(0, slackVars)]
        if typeRest[i] == ">=":
            s[i] = -1
        if typeRest[i] == "<=":
            s[i] = 1
        B[i] = B[i] + s
    return B

def printMatricialModel(C, b, X, A, R, Xs, B):
    print("\nC = \n", np.array(C))
    print("\nb = \n", np.array(b))
    print("\nX = \n", np.array(X))
    print("\nP = \n", np.array(A))
    print("\nXs = \n", np.array(Xs))
    print("\nB = \n", np.array(B))
    print("\n", np.array(R), ">= 0")

def getXb(B, b):
    return np.dot(np.linalg.inv(B), np.array(b))

def printIteration(Cb, B, A, C, b, Zeros):
    ops = [[0, 0, 0, 0], [0, 0, 0, 0]]
    ops[0][0] = str(np.array([1]))
    ops[0][1] = str(np.dot(np.dot(Cb, np.linalg.inv(B)), A)-C)
    ops[0][2] = str(np.dot(Cb, np.linalg.inv(B)))
    ops[0][3] = str(np.dot(np.dot(Cb, np.linalg.inv(B)), b))
    ops[1][0] = str(Zeros)
    ops[1][1] = str(np.dot(np.linalg.inv(B), A))
    ops[1][2] = str(np.linalg.inv(B))
    ops[1][3] = str(np.dot(np.linalg.inv(B), b))
    print("\nZ = ", ops[0][3])
    print("\n", tabulate(ops, headers=["Columna 1", "Columna 2", "Columna 3", "Columna 4"], tablefmt="grid"))

def Solution():
    print("")
    numVars = int(input("Ingrese la cantidad de variables de decisión del problema: "))
    numRest = int(input("Ingrese la cantidad de restricciones del problema: "))
    obj = input("¿Cuál es el objetivo de la función (Max - Min)?: ")
    coefsZ = getZCoefs(numVars)
    coefsRest = getRestrictCoefs(numRest, numVars)
    typeRest, slackVars = getTypeRestric(numRest)
    right = getRightSide(numRest)
    Z = getZ(coefsZ)
    Rest = getRestrictions(numRest, coefsRest, numVars, typeRest, right)
    # Imprimimos la forma canónica del módelo
    printCanonModel(obj, Z, Rest)
    estZ = getEstandarZ(Z, slackVars)
    estRest = getEstandarRestric(numRest, coefsRest, numVars, typeRest, right)
    # Imprimimos la forma estándar del módelo
    printEstandarModel(obj, estZ, estRest)
    # Empezamos a formar el módelo matricial
    C = coefsZ
    X, R = getXandR(numVars, slackVars)
    b = getb(right)
    A = getA(numRest, coefsRest, slackVars, typeRest)
    Xs = [["S" + str(i + 1)] for i in range(0, numRest)]
    B = getB(numRest, slackVars, typeRest)
    # Imprimimos nuestro modelo matricial aumentado
    printMatricialModel(C, b, X, A, R, Xs, B)
    Xb = getXb(B, b)
    Cb = [0 for _ in range(0, len(Xb))]
    Zeros = [[0] for _ in range(0, numRest)]
    printIteration(np.array(Cb), np.array(B), np.array(A), np.array(C), np.array(b), np.array(Zeros))

Solution()