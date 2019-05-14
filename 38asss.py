import numpy as np

def letrehoz (sor,oszlop):
    x=np.zeros((sor,oszlop),dtype=str)
    for i in range(x.shape[0]):
        for j in range (x.shape[1]):
            x[i,j]="X"
    return x

def foglal (matrix,monogram,kivant_sor=0,kivant_oszlop=0):
    if kivant_sor > matrix.shape[0] or kivant_oszlop > matrix.shape[1] // 2:
        print("Helytelen pozicio")
        return

    if kivant_oszlop ==0 or kivant_sor==0:
        for i in range(matrix.shape[0]):
            for j in range(0,matrix.shape[1],2):
                if matrix[i,j] == "X" and matrix[i,j+1]== "X":
                    matrix[i, j]=monogram[0]
                    matrix[i, j+1]=monogram[1]
                    return

    else:
            if matrix[kivant_sor - 1, (kivant_oszlop * 2) - 2] == "X" and matrix[kivant_sor - 1, (kivant_oszlop * 2) - 1]== "X":
                matrix[kivant_sor - 1, (kivant_oszlop * 2) - 2] = monogram[0]
                matrix[kivant_sor - 1, (kivant_oszlop * 2) - 1] = monogram[1]
                return
            else:
                print("A hely foglalt")
                return

    print("Nincs tobb hely")

def keres(matrix,monogram):
    for i in range(matrix.shape[0]):
        for j in range(0, matrix.shape[1], 2):
            if matrix[i, j] == monogram[0] and matrix[i, j + 1] == monogram[1]:
                return [i+1,j+1]
    return -1

def modosit(matrix,monogram,kivant_sor,kivant_oszlop):
    if kivant_sor>matrix.shape[0] or kivant_oszlop>matrix.shape[1]//2:
        print("Helytelen pozicio")
        return
    pozicio=keres(matrix,monogram)
    if pozicio != -1:
        if matrix[kivant_sor - 1, (kivant_oszlop * 2) - 2] == "X" and matrix[kivant_sor - 1, (kivant_oszlop * 2) - 1] == "X":
            matrix[kivant_sor - 1, (kivant_oszlop * 2) - 2] = monogram[0]
            matrix[kivant_sor - 1, (kivant_oszlop * 2) - 1] = monogram[1]
            matrix[pozicio[0], pozicio[1]] = "X"
            matrix[pozicio[0], pozicio[1] + 1] = "X"
            return
        else:
            print("A hely foglalt")
            return

def torles(matrix,monogram):
    pozicio=keres(matrix,monogram)
    if pozicio!=-1:
        matrix[pozicio[0], pozicio[1]] = "X"
        matrix[pozicio[0], pozicio[1] + 1] = "X"

Mozi=letrehoz(40,100)
foglal(Mozi,'SD',3,1)
print(Mozi)
print(keres(Mozi,'SD '))
modosit(Mozi,'SD',2,3)
print(Mozi)
torles(Mozi,'SD')
print()
print(Mozi)





