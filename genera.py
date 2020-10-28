"""
Angelica Gisselle Garcia Espindola
Alexis López Lira


En el comentario del archivo anterior, hice varias cosas, 
para poder sacar la matriz de probabilidades, 
ahora hay que hacer un programa que a partir de 10 tweets genere la misma 
matriz de probabilidades
sabiendo de ante mano cuales son los de stream

Sugiero esta estructura, para lo tweets

{
	"Tweets" : [
		{"Stream":true, "texto":"Vamos a darle a Among Us con famosos"},
		{"Stream":false, "texto":"El Fugitivo: La Historia en 1 Video"},
	]
}

y debe generar el  json compatible con el programa de clasificacion

"""

import json
Data = False

def contar(L, P):
	total = 0
	for e in L:
		if e == P:
			total += 1
	return total

def buscar(L,P):
	total = 0
	if L != False:
		for e in L:
			teewt = e['texto']
			total += teewt.count(P)
	return total


with open('base.json','r') as readJson:
	datos = json.load(readJson)
	Data = datos['Tweets']

Elemento = [e for e in Data if e['Stream'] == True]
palabra = ""
Tokens = []
TokensNoRepet = []
if Elemento != False:
	for e in Elemento:
		teewt = e['texto']
		for i in teewt:
			if i != ' ':
				palabra = palabra + i
			else:
				if len(palabra) > 3:
					Tokens.append(palabra)
					if not palabra in TokensNoRepet:
						TokensNoRepet.append(palabra)
				palabra = ""

Aparece = []
if Tokens != False or Tokens != []:
	for i in TokensNoRepet:
		R = contar(Tokens, i)
		Aparece.append(R)

#noAparece = []
#for i in TokensNoRepet:
#	noAparece.append(len(Elemento) - (buscar(Elemento,i)))


lista = []
for i in TokensNoRepet:
	lista.append([i,(Aparece[TokensNoRepet.index(i)] / len(Elemento) )])

data = {}
data['Probabilidades'] = []

for i in lista:
	data['Probabilidades'].append(i)

with open('data.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False)
