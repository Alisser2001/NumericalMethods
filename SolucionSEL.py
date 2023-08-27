import numpy as np
import scipy as sp

#A = np.array([[1, -2, 1], [-2, 4, 0], [3, 1, -1]])
B = np.array([[7], [-8], [2]])
A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
#P = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
#L = np.array([[1, 0, 0], [3, 1, 0], [-2, 0, 1]])
#U = np.array([[1, -2, 1], [0, 7, -4], [0, 0, 2]])


def AlgorithmSEL(U, C):
    X = np.ravel(np.linalg.solve(U, C))
    result = ["X" + str(np.where(X == value)[0][0]+1) + ": " + str(round(value)) for value in np.ravel(X)]
    return np.ravel(result)

def AlgorithmCholesky(A):
    return sp.linalg.cholesky((A))

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

def AlgorithmPB(P, B):
    return np.dot(P, B)

def AlgorithmC(L, PB):
    return np.linalg.solve(L, PB)


L = AlgotithmL(A)
U = AlgotithmU(A)
P = AlgotithmP((A))
if np.array_equal(A, A.T):
    Up = AlgotithmUp((L))
D = AlgorithmD(U)
PB = AlgorithmPB(P, B)
C = AlgorithmC(L, PB)
X = AlgorithmSEL(U, C)
if np.array_equal(A, A.T):
    V = AlgorithmCholesky(A)
    Vt = V.T

from tabulate import tabulate

data = [
    ["A", "None", A],
    ["L", "AlgorithmL(A)", L],
    ["U", "AlgorithmU(A)", U],
    ["P", "AlgorithmP(A)", P],
    ["U'", "AlgorithmUp(L)", Up] if np.array_equal(A, A.T) else ["U'", "None", "A Asymmetric"],
    ["D", "AlgorithmD(U)", D],
    ["PB", "AlgorithmPB(P, B)", PB],
    ["C", "AlgorithmC(L, PB)", C],
    ["V", "AlgorithmCholesky(A)", V] if np.array_equal(A, A.T) else ["V", "None", "A Asymmetric"],
    ["Vt", "V.T", Vt] if np.array_equal(A, A.T) else ["Vt", "None", "A Asymmetric"],
    ["X", "AlgorithmSEL(U, C)", X],
]

print("\n", tabulate(data, headers=["Variable", "Algoritmo", "Valor"], tablefmt="grid"))