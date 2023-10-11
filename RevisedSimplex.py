def Solution():
    print("")
    numVars = int(input("Ingrese la cantidad de variables de decisión del problema: "))
    numRest = int(input("Ingrese la cantidad de restricciones del problema: "))
    obj = input("¿Cuál es el objetivo de la función (max - min)?: ")
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
    for i in range(0, numRest):
        t = input("Ingresa el tipo de la restriccición " + str(i + 1) + " (>=, ==, <=): ")
        typeRest.append(t)
    right = []
    for i in range(0, numRest):
        val = float(input("Ingresa el valor al lado derecho de la restricción " + str(i+1) + ": "))
        right.append(val)
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

Solution()