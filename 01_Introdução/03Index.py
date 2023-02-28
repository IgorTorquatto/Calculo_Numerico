import numpy as np

#Acesso aos índices:

array = np.array([1,2,3])
print(array[0])

#Podem ser feitas operações matemáticas com os valores dos índices de um array.

#2D:

array2 = np.array([[1,2,3],[4,5,6]])

print(array2)
print(array2[1][1])

#Lembrando da indexação (0->end)

#3D

array3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(array3)
#Access the third element of the second array of the first array:
print(array3[0, 1, 2]) #6