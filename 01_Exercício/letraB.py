from letraA import matpot
import numpy as np

A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
B = np.array([[2,-2,-4],[-1,3,4],[1,-2,-3]])
C = np.array([[0,1,0],[0,0,2],[0,0,0]])

print(matpot(A,30))
print(matpot(B,30))
print(matpot(C,30))
