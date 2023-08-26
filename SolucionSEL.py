import numpy as np

A = np.array([[1, -2, 1], [-2, 4, 0], [3, 1, -1]])
B = np.array([[7], [-8], [2]])
P = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
L = np.array([[1, 0, 0], [3, 1, 0], [-2, 0, 1]])
U = np.array([[1, -2, 1], [0, 7, -4], [0, 0, 2]])


def Algorithm(P, L, U, B):
    PB = np.dot(P, B)
    C = np.linalg.solve(L, PB)
    X = np.ravel(np.linalg.solve(U, C))
    result = ["X" + str(np.where(X == value)[0][0]+1) + ": " + str(round(value)) for value in np.ravel(X)]
    return np.ravel(result)

print(Algorithm(P, A, L, U, B))