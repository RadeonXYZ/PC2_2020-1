def crea_arreglo():
    from random import randint
    m=int(input("Ingrese la cantidad de filas: "))
    n=int(input("Ingrese la cantidad de columnas: "))
    A=[]
    for i in range(m):
        A.append([0]*n)
    for i in range(m):
        for j in range(n):
            A[i][j]=randint (10, 99)
    for i in range(m):
        print(A[i])


def mueve_col():
    import numpy as np
    M = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(M)
    x=int(input("ingrese el numero de columnas q quiere intercambiar(La primera cuena como fila 0): "))
    y=int(input("ingrese el numero de columna q quiere intercambiar la anterior: "))

    if x==0:
        if y==1:
            M[:, [1,0,2,3,4]]
        elif y==2:
            M[:, [2,1,0,3,4]]
        elif y==3:
            M[:, [3,1,0,0,4]]
        elif y==4:
            M[:, [4,1,0,3,0]]
    elif x==1:
        if y==0:
            M[:, [1,0,2,3,4]]
        elif y==2:
            M[:, [0,2,1,3,4]]
        elif y==3:
            M[:, [0,3,2,1,4]]
        elif y==4:
            M[:, [0,4,2,3,1]]
    elif x==2:
        if y==0:
            M[:, [2,1,0,3,4]]
        elif y==1:
            M[:, [0,2,1,3,4]]
        elif y==3:
            M[:, [0,1,3,2,4]]
        elif y==4:
            M[:, [0,1,4,3,2]]
    elif x==3:
        if y==0:
            M[:, [3,1,2,0,4]]
        elif y==1:
            M[:, [0,3,0,1,4]]
        elif y==2:
            M[:, [0,1,3,2,4]]
        elif y==4:
            M[:, [0,1,2,4,3]]
    elif x==4:
        if y==0:
            M[:, [4,1,2,3,0]]
        elif y==1:
            M[:, [0,4,2,3,1]]
        elif y==2:
            M[:, [0,1,4,3,2]]
        elif y==3:
            M[:, [0,1,2,4,3]]
