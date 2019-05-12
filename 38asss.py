import numpy as np

matrix=np.zeros((10,6), dtype=str)

def foglal (matrix,monogram,kivant_sor=0,kivant_oszlop=0):
    if kivant_sor == 0 or kivant_oszlop == 0:
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1], 2):
                if matrix[i,j] == "X" and matrix[i,j+1]== "X":
                    matrix[i,j]=monogram[0]
                    matrix[i,j+1]=monogram[1]

    else:
        matrix[kivant_sor]=monogram[0]
        matrix[kivant_oszlop]=monogram[1]













#print(matrix)
