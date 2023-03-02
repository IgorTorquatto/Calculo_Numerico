import numpy as np

def derivada(coef):
    n = len(coef)
    der = np.zeros(n-1)
    for i in range(n-1):
        der[i] = coef[i] * (n-i-1)
    return der

P = np.array([1, -210, 20615, 1256850, 53327946])
print(derivada(P))

