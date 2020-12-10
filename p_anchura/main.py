
import json
Arbol = False

with open ("base.json","r") as read_file:
	data = json.load(read_file)
	Arbol = data['arbol']

def hijos(valor):
    l = []
    l2 = []
    j = 0
    for e in Arbol:
        valorN = e[1]
        l.append(valorN.split())
        l2.append(e[0])
    
    for i in l:
        #print(l2[j], l[j][0])
        if l[j][0] == valor:
            return True
        j = j + 1

respuesta = hijos("33")
if(respuesta == True):
	print (" si está en el arbol")
