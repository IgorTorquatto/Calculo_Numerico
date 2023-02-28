import numpy as np

#Slicing array
#[start:end)
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) #[2,3,4,5]

print(arr[1:]) #[2 até o final]

print(arr[:4]) #fatiar até o indice 4 , não incluido