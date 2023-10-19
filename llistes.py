def LlegirLlista(n_elements):
    llista = []
    for i in range (n_elements):
        llista.append(int(input("Introdueix un valor a la llista: ")))
    return llista

def InicialitzarLlista(n_elements,valor):
    llista = []
    for i in range (n_elements):
        llista.append(valor)
    return llista

def MitjanaLlista(llista):
    suma = 0
    for i in range(len(llista)):
        suma += llista[i]
    mitjana = suma/len(llista)
    return mitjana

def MaximLlista(llista):
    valormax=llista[0]
    posmax=0
    for i in range(len(llista)):
        if llista[i]>valormax:
            valormax=llista[i]
            posmax = i
    return posmax

def MinimLlista(llista):
    valormin=llista[0]
    posmin=0
    for i in range(len(llista)):
        if llista[i]<valormin:
            valormin=llista[i]
            posmin = i
    return posmin
    
def MinimLlistaNoZero(llista):
    minim = 100000
    posmin = 0
    for i in range((len(llista))):
        if llista[i]<minim and llista[i]>0:
            minim = llista[i]
            posmin = i
    if minim == 100000:
        posmin = -1
    return posmin
