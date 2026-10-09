import numpy as np

# Matriz original
#matriz = np.array([[0, ((2)**0.5)/2, -((2)**0.5)/2], [((2)**0.5)/2, 1/2, 1/2], [((2)**0.5)/2, -1/2, -1/2]])
matriz_teste = np.array([[1,2,0],[3,4,0],[0,0,0]])

# Obtendo a transposta
T = matriz_teste.T
print(T)

determinante = np.linalg.det(matriz_teste)

print(f"Determinante da matriz: {determinante:.2f}")

#Realiza o produto matricial entre as duas matrizes
#print(np.dot(matriz, T))

