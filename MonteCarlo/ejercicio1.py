import random, math

ptosInR1=0
ptosInR2=0
nsim=100000
for i in range(0,nsim):
    x=random.random() #U(0,1)
    y=random.random() #U(0,1)

    if x**2 + y**2 <= 1:
        ptosInR1+=1
        if x <= 0.6:
            ptosInR2+=1
    
areaR1=4*float(ptosInR1)/float(nsim)
areaR2=4*float(ptosInR2)/float(nsim)

errorR1=abs(areaR1-1./3.)
errorR2=abs(areaR2-1./3.)
print('Area= ', areaR1, '  error= ', errorR1,'Nsim='+str(nsim) + '\n')
print('Area= ', areaR2, '  error= ', errorR2,'Nsim='+str(nsim) + '\n')