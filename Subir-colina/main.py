import json

Datos = False

with open('datosColina.json','r') as info:
    data = json.load(info)
    Datos = data["Datos"]

def definirCamino(camino):
    valorAnterior = 0
    valorMenor = 0
    L = []
    for i in camino:
        if valorAnterior == 0:
            L.append(i)
            valorAnterior = i[2]
        else:
            if i[2] <= valorAnterior:
                valorMenor = i[2]
                valorAnterior = i[2]
                L = []
                L.append(i)
            else:
                valorMenor = valorAnterior
                valorAnterior = i[2]
    return L


def subirColina():
    listaRetorno = []
    camino = []
    valor = str(input('Escrbe un valor: ')).upper()
    if valor == "":
        return "Debes escribir un dato"
    if valor == Datos[0][0]:
        return valor,"Es el nodo raíz"
    Elemento = [ e for e in Datos if e[1] == valor]
    listaRetorno.append(Elemento[0])
    while Elemento[0][0] != Datos[0][0]:
        Elemento = [ e for e in Datos if e[1] == Elemento[0][0]]
        if len(Elemento) > 1:
            Elemento = definirCamino(Elemento)
            listaRetorno.append(Elemento[0])
        else:
            listaRetorno.append(Elemento[0])
    return listaRetorno


A = subirColina()
if type(A) == list:
    A = A[::-1]
print("Camino a seguir: ",A)
