import numpy as np
import scipy as sp
from tabulate import tabulate

def AlgorithmSEL(U, C):
    # np.ravel(np.linalg.solve(U, C))
    n = len(C)
    X = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        X[i][0] = (C[i][0] - sum(U[i][j] * X[j][0] for j in range(i + 1, n))) / U[i][i]
    result = ["X" + str(np.where(X == value)[0][0]+1) + ": " + str(round(value)) for value in np.ravel(X)]
    return np.ravel(result)

def AlgorithmPB(P, B):
    #np.dot(P, B)
    filasP = len(P)
    columnasP = len(P[0])
    filasB = len(B)
    columnasB = len(B[0])
    PB = np.array([[0 for _ in range(columnasB)] for _ in range(filasP)])
    if columnasP == filasB:
        for i in range(0, filasP):
            for j in range(0, columnasB):
                for k in range(0, columnasP):
                    PB[i][j] += P[i][k] * B[k][j]
        return PB
    else:
        return PB

def AlgorithmC(L, PB):
    #np.linalg.solve(L, PB)
    n = len(PB)
    C = np.zeros((n, 1))
    for i in range(n):
        C[i][0] = (PB[i][0] - sum(L[i][j] * C[j][0] for j in range(i))) / L[i][i]
    return C

def AlgorithmCholesky(L, D):
    return np.dot(L, np.sqrt(D))

def AlgotithmL(A):
    _, L, _ = sp.linalg.lu(A)
    return L

def AlgotithmU(A):
    _, _, U = sp.linalg.lu(A)
    return U

def AlgotithmP(A):
    P, _, _ = sp.linalg.lu(A)
    return P

def AlgotithmUp(L):
    return L.T

def AlgorithmD(U):
    return np.diag(np.diag(U))

def Solution(A, B, L = None, U = None, P = None):
    if L is None:
        L = AlgotithmL(A)
    if U is None:
        U = AlgotithmU(A)
    if P is None:
        P = AlgotithmP(A)
    if np.array_equal(A, A.T):
        Up = AlgotithmUp((L))
    D = AlgorithmD(U)
    if np.array_equal(A, A.T):
        V = AlgorithmCholesky(L, D)
        Vt = V.T
    PB = AlgorithmPB(P, B)
    C = AlgorithmC(L, PB)
    X = AlgorithmSEL(U, C)
    data = [
        ["A", "None", A],
        ["L", "AlgorithmL(A)", L],
        ["U", "AlgorithmU(A)", U],
        ["P", "AlgorithmP(A)", P],
        ["PA", "np.dot(P, A)", np.dot(P, A)],
        ["LU", "np.dot(L, U)", np.dot(L, U)],
        ["U'", "AlgorithmUp(L)", Up] if np.array_equal(A, A.T) else ["U'", "None", "A Asymmetric"],
        ["D", "AlgorithmD(U)", D],
        ["PB", "AlgorithmPB(P, B)", PB],
        ["C", "AlgorithmC(L, PB)", C],
        ["V", "AlgorithmCholesky(A)", V] if np.array_equal(A, A.T) else ["V", "None", "A Asymmetric"],
        ["Vt", "V.T", Vt] if np.array_equal(A, A.T) else ["Vt", "None", "A Asymmetric"],
        ["VVt", "np.dot(V, Vt)", np.dot(V, Vt)] if np.array_equal(A, A.T) else ["VVt", "None", "A Asymmetric"],
        ["X", "AlgorithmSEL(U, C)", X],
    ]
    print("\n", tabulate(data, headers=["Variable", "Algoritmo", "Valor"], tablefmt="grid"))

def UserInfo():
    print("Ingresa el tamaño de la matriz A cuadrada: ")
    n = int(input())
    A = np.zeros((n, n))
    B = np.zeros((n, 1))
    for i in range(0, n):
        for j in range(0, n):
            print("Ingresa el valor de la posición A" + str(i) + str(j) + ": ")
            A[i][j] = float(input())
    print("")
    for i in range(0, n):
        print("Ingresa el valor de la posición B" + str(i) + str(0) + ": ")
        B[i][0] = float(input())
    print("\nA:\n", A)
    print("\nB:\n", B)
    print("\n¿Ya conoces la factorización PA = LU de la matriz A? s(Sí)  n(No): ")
    r = input()
    if r == "n":
        Solution(A, B)
    if r == "s":
        L = np.zeros((n, n))
        U = np.zeros((n, n))
        P = np.zeros((n, n))
        for i in range(0, n):
            for j in range(0, n):
                print("Ingresa el valor de la posición L" + str(i) + str(j) + ": ")
                L[i][j] = float(input())
        print("")
        for i in range(0, n):
            for j in range(0, n):
                print("Ingresa el valor de la posición U" + str(i) + str(j) + ": ")
                U[i][j] = float(input())
        print("")
        for i in range(0, n):
            for j in range(0, n):
                print("Ingresa el valor de la posición P" + str(i) + str(j) + ": ")
                P[i][j] = float(input())
        print("")
        print("\nL:\n", L)
        print("\nU:\n", U)
        print("\nP:\n", P)
        Solution(A, B, L, U, P)

UserInfo()

#A = np.array([[1, -2, 1], [-2, 4, 0], [3, 1, -1]])
#A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
#B = np.array([[7], [-8], [2]])
#L = np.array([[1, 0, 0], [3, 1, 0], [-2, 0, 1]])
#U = np.array([[1, -2, 1], [0, 7, -4], [0, 0, 2]])
#P = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])






