import json

#Valores del Json
Posibilidades = eInicial = eFinal = False

Mat=[[0,1,2], [3,4,5], [6,7,8]]

with open ("baseC.json","r") as read_file:
	data = json.load(read_file)
	Posibilidades = data['grafo']
	eInicial = data['inicio']
	eFinal = data['final']

#buscar mover el caballo
def bCaballo(x,y,D,Matriz,r):
	e = Mat[x][y]
	for i in Posibilidades:
		if (e == i[0]):
			x = 0
			while(x <= 2):
				y = 0
				while(y <= 2):
					if Mat[x][y] == i[r]:
						Matriz[x][y] = D
						return Matriz
					y = y + 1
				x = x + 1


#Mover los caballos
def cab(MInicial,MFinal,r):
    if r == 0:
        r = 1
    else:
        r = 2
    Matriz=[[0,0,0],[0,0,0],[0,0,0]]
    x = 0
    for x in range(len(Matriz)):
        if x < len(Matriz):
            y = 0
            for y in range(len(Matriz)):
                if y < len(Matriz):
                    if MInicial[x][y] != 0:
                        D = MInicial[x][y]
                        MInicial[x][y] = 0
                        bCaballo(x,y,D, Matriz, r)
                y = y + 1
            x = x + 1

    for e in Matriz:
        print (e)
    print ("========== CAMBIO =============")
    
    if (Matriz != eFinal):
        return cab(Matriz,MFinal,r)


print("Recorrer derecha escribe 0 o Recorrer izquierda escribe 1: ")
r = int(input())
if (r < 0 or r > 1):
	print ("Escribe un valor correcto.")
else:
    cab(eInicial,eFinal,r)
