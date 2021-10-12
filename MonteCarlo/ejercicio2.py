# Autores:
# Diego Carballido Álvarez (diego.carballido.alvarez@udc.es)
# José Antonio Figueiras Martínez (jose.figueirasm@udc.es)

import random, math

alturaCilindro = 1/2

ptosCircunfCilindro = 0
ptosCircunfCentro = 0
ptosCircunfInferior = 0
ptosCircunfSuperior = 0
ptosRuedaEsferica = 0

radioCircunfCilindro = 1/2
radioCircunfSuperior = 2
radioCircunfCentro = 4
radioCirunfInferior = 1
radioRuedaEsferica = 1/3
nsim=2000000

#def f(x, y):
#    return math.sqrt(radioCircunfCentro**2 - x**2 -y**2)

def volumenCubo(lado):
    return lado**3

def volumenEsferaParaError(radio):
    return 4/3*math.pi*radio**3

for i in range(0,nsim):

    x=random.uniform(0, 1) #U(0,1/2)
    y=random.uniform(0, 1) #U(0,1/2)

    if x**2 + y**2 <= radioCircunfCilindro**2:
        ptosCircunfCilindro += 1

    x=random.uniform(0, radioCircunfSuperior) #U(0,2)
    y=random.uniform(0, radioCircunfSuperior) #U(0,2)
    z=random.uniform(0, radioCircunfSuperior) #U(0,2)

    if x**2 + y**2 + z**2 <= radioCircunfSuperior**2:
        ptosCircunfSuperior += 1

    x=random.uniform(0, radioCircunfCentro) #U(0,4)
    y=random.uniform(0, radioCircunfCentro) #U(0,4)
    z=random.uniform(0, radioCircunfCentro) #U(0,4)

    if x**2 + y**2 + z**2 <= radioCircunfCentro**2:
        ptosCircunfCentro += 1

    x=random.uniform(0, radioCirunfInferior) #U(0,1)
    y=random.uniform(0, radioCirunfInferior) #U(0,1)
    z=random.uniform(0, radioCirunfInferior) #U(0,1)

    if x**2 + y**2 + z**2 <= radioCirunfInferior**2:
        ptosCircunfInferior += 1

    x=random.uniform(0, radioRuedaEsferica) #U(0,1/3)
    y=random.uniform(0, radioRuedaEsferica) #U(0,1/3)
    z=random.uniform(0, radioRuedaEsferica) #U(0,1/3)

    if x**2 + y**2 + z**2 <= radioRuedaEsferica**2:
        ptosRuedaEsferica += 1

pSuperior = float(ptosCircunfSuperior)/float(nsim)    
pCentro = float(ptosCircunfCentro)/float(nsim)
pInferior = float(ptosCircunfInferior)/float(nsim)
pRueda = float(ptosRuedaEsferica)/float(nsim)

# Cilindros superiores
areaCircunfCilindroSuperior = 4*float(ptosCircunfCilindro)/float(nsim)
print(areaCircunfCilindroSuperior)
volumenCilindroSuperior = areaCircunfCilindroSuperior * alturaCilindro
volumenCilindrosSuperiores = volumenCilindroSuperior*2
errorCilindrosSuperiores = abs(volumenCilindrosSuperiores - math.pi*radioCircunfCilindro**2*alturaCilindro*2)

# Semiesfera superior
volumenCircunfSuperior = pSuperior * volumenCubo(radioCircunfSuperior*2)
volumenSemiesferaSuperior = volumenCircunfSuperior/2
errorCirunfSuperior = abs(volumenSemiesferaSuperior - volumenEsferaParaError(radioCircunfSuperior)/2)

# Esfera central
volumenCircunfCentro = pCentro * volumenCubo(radioCircunfCentro*2)
errorCirunfCentro = abs(volumenCircunfCentro - volumenEsferaParaError(radioCircunfCentro))

# Semiesfera inferior
volumenCircunfInferior = pInferior * volumenCubo(radioCirunfInferior*2)
volumenSemiesferaInferior = volumenCircunfInferior/2
errorCirunfInferior = abs(volumenSemiesferaInferior - volumenEsferaParaError(radioCirunfInferior)/2)

# Ruedas inferiores
volumenRueda = pRueda * volumenCubo(radioRuedaEsferica*2)
volumenRuedas = volumenRueda * 3
errorRuedas = abs(volumenRuedas - volumenEsferaParaError(radioRuedaEsferica)*3)

print('Volumen cilindros superiores = ', volumenCilindrosSuperiores, 'Error = ', errorCilindrosSuperiores, 'Nsim ='+str(nsim) + '\n')
print('Volumen semiesfera superior = ', volumenSemiesferaSuperior, 'Error = ', errorCirunfSuperior, 'Nsim ='+str(nsim) + '\n')
print('Volumen circunferencia centro = ', volumenCircunfCentro, 'Error = ', errorCirunfCentro, 'Nsim ='+str(nsim) + '\n')
print('Volumen semiesfera inferior = ', volumenSemiesferaInferior, 'Error = ', errorCirunfInferior, 'Nsim ='+str(nsim) + '\n')
print('Volumen ruedas inferiores = ', volumenRuedas, 'Error = ', errorRuedas, 'Nsim ='+str(nsim) + '\n')
print('Volumen total = ', volumenCilindrosSuperiores + volumenSemiesferaSuperior + volumenCircunfCentro + 
            volumenSemiesferaInferior + volumenRuedas, 'Error = ', errorCilindrosSuperiores + errorCirunfSuperior + 
            errorCirunfCentro + errorCirunfInferior + errorRuedas, 'Nsim ='+str(nsim) + '\n')