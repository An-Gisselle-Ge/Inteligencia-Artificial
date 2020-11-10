valores={
	"5":"10",
	"15":"10",
	"1":"5",
	"9":"5",
	"14":"15",
	"16":"15",
	"30":"16"
}

camino=[]

def buscar(inicio, valorBuscar):
	camino.append(inicio)
	if inicio==valorBuscar:
		return valorBuscar
	
	for k,v in valores.items():
		if v==inicio:
			result = buscar(k,valorBuscar)
			if result:
				return result
	red=camino.pop()
	return 0
	
origen = input("Ingresa el nodo origen: ")
destino = input("Ingresa el nodo destino: ")
	
result = buscar(origen,destino)
	
if result:
	print(camino)
else:
	print("No encontrado")
