# Autores:
# Diego Carballido Álvarez (diego.carballido.alvarez@udc.es)
# José Antonio Figueiras Martínez (jose.figueirasm@udc.es)

import matplotlib.pyplot as plt
import numpy as np

#funcion recurvisa
def B(coorArr, i, j, t):
    if j == 0:
        return coorArr[i]
    return B(coorArr, i, j - 1, t) * (1 - t) + B(coorArr, i + 1, j - 1, t) * t

#Puntos de control
P=np.array([[0.75, 1.5],[1., 1.],[2.,1.],[2.75,1.],[3.,1.5],[3.1,1.75],
            [3.,2.],[2.75,2.5],[2.,2.5],[1.,2.5],[0.75,2.],[0.75,1.75],
            [0.75,1.5],[0.75,1.],[1.,0.5],[1.5,0.],[2.,0.],[2.75,0.],[3.,0.25]])  

fig=plt.figure("Letra e")

ini=0; fin=3
#Una iteración del for por cada curva
for k in range(0,9):
    x=P[ini:fin,0]
    y=P[ini:fin,1]
    n=x.size
    
    xb=[]
    yb=[]
    for t in np.linspace(0.,1.,25):
        a = B(x, 0, n - 1, t)
        b = B(y, 0, n - 1, t)
        xb.append(a)
        yb.append(b)
    plt.plot(xb,yb)
    ini=fin-1
    fin=ini+n

plt.plot(P[:,0],P[:,1],'c--',P[:,0],P[:,1],'ko',ms=8)

plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.axis([min(P[:,0])-0.065,max(P[:,0])+.05,min(P[:,1])-0.05,max(P[:,1])+0.05])
plt.show()