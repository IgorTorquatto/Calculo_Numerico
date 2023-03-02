import numpy as np

def matpot(A,k):
    """
    Calcula a k-ésima potência da matriz A.
    
       Argumentos:
         A (numpy.array): matriz quadrada armazenada usando o `array` da numpy.
         k (int): valor da potência desejada, k >= 0.
         
       Retorno:
         (numpy.array): o valor de A^k
    """
    # você deve iniciar a implementação desta função a partir daqui.
    
    if (k<0):
        print("Número de expoente inválido.")
        return

    numeroLinhas = A.shape[0]
    numeroColunas = A.shape[1]

    if (k==0):
    #Matriz elevado a 0 igual a identidade
        matrizIdentidade = np.eye(numeroLinhas,dtype= int)
        return matrizIdentidade
    
    if(k==1):
    #Retorna ela mesma
        return A
    
    aux = A
    
    for i in range (1,k):
        aux = np.dot(A,aux)
    
    return aux


matrizA = np.array([[1,1],[1,1]])

print(matpot(matrizA,-1))
print("\n")
print(matpot(matrizA,0))
print("\n")
print(matpot(matrizA,1))
print("\n")
print(matpot(matrizA,2))
print("\n")
print(matpot(matrizA,3))
print("\n")
print(matpot(matrizA,4))
