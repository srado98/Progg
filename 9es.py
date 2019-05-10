import numpy as np
import random
import sys


n1=2
n2=3
n3=3
n4=2

a=np.random.random((n1,n2));
b=np.random.random((n3,n4));
s=(n1,n4)
szorzat=np.zeros(s)
if n2!=n3:
    print("A két mátrix nem szorozható össze")

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            szorzat[i][j]+=a[i][k]*b[k][j]


print("A matrix:\n",a)
print("B mátrix:\n",b)
print("A szorzatuk:\n",szorzat)


