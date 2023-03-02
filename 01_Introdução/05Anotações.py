import numpy as np

print(np.e)

A= np.array([[1,2,3],[4,5,6]])

print(A) #Para se ter uma matriz usamos os colchetes

print(A.shape[1])

B = np.array([[7, 1, 3, 0],[6, 0, 2, 6],[2, 2, 1, 9],[8, 6, 7, 1]])

print(B+1) # Ao somar um elemento à matriz soma em todas as posições

A = np.array([[1, 1, 1, 1],[2, 2, 2, 2],[3, 3, 3, 3],[4, 4, 4, 4]])
B = np.array([[7, 1, 3, 0],[6, 0, 2, 6],[2, 2, 1, 9],[8, 6, 7, 1]])

print(A)
print(B)
print(np.dot(A,B)) # Resultado multiplicação

#Se dois arranjos  𝐯 e  𝐰 forem unidimensionais (vetor linha), o resultado será o produto escalar entre eles:

v = np.array([1, 1, 1, 1])
w = np.array([7, 1, 3, 0])

print(np.dot(v,w))