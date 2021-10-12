import random

ptosInR1 = 0
ptosInR2 = 0
ptosCirculoInterno = 0
radioCirculoInterno = 0.5
nsim=100000
for i in range(0,nsim):
    x=random.random() #U(0,1)
    y=random.random() #U(0,1)

    sumaDeCuadrados = x**2 + y**2
    if sumaDeCuadrados <= radioCirculoInterno**2:
        ptosCirculoInterno += 1
    if sumaDeCuadrados <= 1:
        ptosInR1 += 1
        if x <= 0.6:
            ptosInR2+=1
    
areaR1 = 4*float(ptosInR1)/float(nsim)
areaR2 = 4*float(ptosInR2)/float(nsim)
areaCirculoInterno = 4*float(ptosCirculoInterno)/float(nsim)
areaR3 = areaR2 - areaCirculoInterno

print('AreaR1 = ', areaR1, 'Nsim ='+str(nsim) + '\n')
print('AreaR2 = ', areaR2, 'Nsim ='+str(nsim) + '\n')
print('AreaR3 = ', areaR3, 'Nsim ='+str(nsim) + '\n')