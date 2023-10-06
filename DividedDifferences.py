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
            val = val + "X" + str(i+j+1) + ", "
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
    coefPol = []
    varPol = []
    for i in range(0, len(pts)-1):
        varPol.append("(X - "+str(pts[i][0])+")")
    coefPol.append(pts[0][1])
    for i in range(0, len(ops)):
        coefPol.append(ops[i][0][1])
    P = ""
    for i in range(0, len(coefPol)):
        vars = ""
        for j in range(0, i):
            vars += varPol[j]
        P = P + "(" + str(coefPol[i]) + ")" + vars + (" + " if i < len(coefPol) - 1 else "")
    print("P(x) = " + str(P))
Solution()