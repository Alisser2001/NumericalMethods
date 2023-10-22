import numpy as np

def Solution():
    print("")
    numVars = int(input("Ingrese la cantidad de variables de decisión del problema: "))
    numRest = int(input("Ingrese la cantidad de restricciones del problema: "))
    obj = input("¿Cuál es el objetivo de la función (Max - Min)?: ")
    coefsZ = []
    for i in range(0, numVars):
        coef = float(input("Ingresa el valor del coeficiente de X" + str(i+1) + " en Z: "))
        coefsZ.append(coef)
    coefsRest = []
    for i in range(0, numRest):
        for j in range(0, numVars):
            coef = float(
                input("Ingresa el valor del coeficiente de X" + str(j + 1) + " en la restricción " + str(i + 1) + ": "))
            coefsRest.append((i, "X" + str(j + 1), coef))
    typeRest = []
    slackVar = 0
    for i in range(0, numRest):
        t = input("Ingresa el tipo de la restriccición " + str(i + 1) + " (>=, ==, <=): ")
        if t == "<=" or  t == ">=":
            slackVar += 1
        typeRest.append(t)
    right = []
    for i in range(0, numRest):
        val = float(input("Ingresa el valor al lado derecho de la restricción " + str(i+1) + ": "))
        right.append([val])
    Z = ""
    for i in range(0, len(coefsZ)):
        Z = Z + "(" + str(coefsZ[i]) + ")" + "X" + str(i+1) + (" + " if i < len(coefsZ) - 1 else "")
    print(" ")
    print(obj + " Z = " + Z)
    Rest = ["" for _ in range(numRest)]
    for i in range(0, len(coefsRest)):
        Rest[coefsRest[i][0]] = Rest[coefsRest[i][0]] + "(" + str(coefsRest[i][2]) + ")" + coefsRest[i][1] + (" + " if int(coefsRest[i][1][1]) < numVars else "")
    for i in range(0, len(Rest)):
        Rest[i] = Rest[i] + " " + typeRest[i] + " " + str(right[i])
    for i in range(0, len(Rest)):
        print("Rest " + str(i+1) + ": " + Rest[i])
    print("\nForma Estandar: ")
    for i in range(0, slackVar):
        Z = Z + " + (0)" + "S" + str(i+1)
    print(" ")
    print(obj + " Z = " + Z)
    Rest = ["" for _ in range(numRest)]
    for i in range(0, len(coefsRest)):
        Rest[coefsRest[i][0]] = Rest[coefsRest[i][0]] + "(" + str(coefsRest[i][2]) + ")" + coefsRest[i][1] + (" + " if int(coefsRest[i][1][1]) < numVars else "")
    for i in range(0, len(Rest)):
        if typeRest[i] == ">=":
            Rest[i] = Rest[i] + " - (1.0)S" + str(i+1)
        if typeRest[i] == "<=":
            Rest[i] = Rest[i] + " + (1.0)S" + str(i+1)
    for i in range(0, len(Rest)):
        Rest[i] = Rest[i] + " == " + str(right[i])
    for i in range(0, len(Rest)):
        print("Rest " + str(i + 1) + ": " + Rest[i])
    C = coefsZ
    b = []
    for i in range(0, len(right)):
        b.append(right[i])
    X = []
    R = []
    for i in range(0, numVars):
        X.append(["X" + str(i+1)])
        R.append("X" + str(i+1))
    for i in range(0, slackVar):
        R.append("S" + str(i+1))
    P = [[] for _ in range(0, numRest)]
    for i in range(0, len(coefsRest)):
        P[coefsRest[i][0]].append(coefsRest[i][2])
    for i in range(0, len(P)):
        s = [0 for _ in range(0, slackVar)]
        if typeRest[i] == ">=":
            s[i] = -1
        if typeRest[i] == "<=":
            s[i] = 1
        P[i] = P[i] + s
    print("\nC = \n", np.array(C))
    print("b = \n", np.array(b))
    print("X = \n", np.array(X))
    print("P = \n", np.array(P))
    print(np.array(R), ">= 0")
    Xs = [["S"+str(i+1)] for i in range(0, numRest)]
    Xb = [["X"+str(i+1)] for i in range(0, numRest)]
    Cb = [0 for _ in range(0, numRest)]
    B = [P[i][numVars:-1] + [P[i][-1]] for i in range(0, len(P))]
    print("\nXs = \n", np.array(Xs))
    print("Xb = \n", np.array(Xb))
    print("Cb = \n", np.array(Cb))
    print("B = \n", np.array(B))
    BI = np.linalg.inv(np.array(B))
    print("inv(B) = \n", BI)
    Xb = np.dot(BI, np.array(right))
    print("Xb = \n", Xb)
    Zb = np.dot(np.array(Cb), Xb)
    print("Zb = \n", Zb)

Solution()