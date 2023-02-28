import numpy as np

#0D:

array1= np.array(42)

print(f"Array 0D: ${array1}")

#1D

array2= np.array([1,2,3])

print(f"Array 1D: ${array2}")

#2D

array3= np.array([[1,2,3],[4,5,6]])

print(f"Array 2D: ${array3}")

#3D

array4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(f"Array 3D: ${array4}")

#Assim criamos as matrizes

#Checar a dimensão:

print("Dimensão da Matriz 3: {}".format(array3.ndim))

#Definir o tamanho antes de definir todos os valores:

arraydim5= np.array([1,2,3],ndmin=5)
print(f"Dimensão do array: ${arraydim5.ndim}")