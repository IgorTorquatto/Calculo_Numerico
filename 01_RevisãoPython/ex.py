#Listas

B= [5,2,7]

A= B

A[2] = "texto"

print(A)
print(B)

#A e B estão associados ao meso objeto, logo uma mudança em A aplicará efeitos em B também


C = [5,2,7]

D = C[:]

D[2]= "text"

print(C)
print(D)

#Agora os objetos são diferentes, e assi as litas serão diferentes, isso ocorre devido a função de fatiamento que cria uma copia de C em D.
