
def horizontal(fila,col,matriz):
	while(col <= 3):
		if (matriz[fila][col] == 0):
			matriz[fila][col] = 2
		col = col + 1

def vertical(fila,col,matriz):
	while(fila <= 3):
		if (matriz[fila][col] == 0):
			matriz[fila][col] = 2
		fila = fila + 1

def diagonalder_izq(fila,col,matriz):
	while(fila <= 3 and col <= 3):
		if (matriz[fila][col] == 0):
			matriz[fila][col] = 2
		fila = fila + 1
		col = col + 1

def diagonalizq_der(fila,col,matriz):
	while(fila <= 3 and col >= 0):
		if (matriz[fila][col] == 0):
			matriz[fila][col] = 2
		fila = fila + 1
		col = col - 1

def colocarReinas(fila,col):
	matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	r = 0

	#evaluar si se pueden colocar reinas
	while r != 4 and fila < 4:
		while matriz[fila][col] != 0:
			if col != 3:
				col = col + 1
			else:
				if fila != 3:
					fila = fila + 1
					col = 0
		#colocar reina en espacio en 0
		matriz[fila][col] = 1
		#Rellenar con  2 de todas las formas posibles.
		horizontal(fila,0,matriz)
		vertical(0,col,matriz)
		diagonalder_izq(fila,col,matriz)
		diagonalizq_der(fila,col,matriz)
		#Actualizar los nuevos valores
		fila = fila + 1
		col = 0
		r = r + 1
	if r < 4:
		#print("entra")
		colocarReinas(0,1)
	if r < 4:
		a = 4 - r
		print("Faltaron de colocar: ",a,"reina")
	print ("nummero de reinas",r)
	for e in matriz:
		print (e)
	print ("")


colocarReinas (1,3)
