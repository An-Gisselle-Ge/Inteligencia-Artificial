######################################################

            #Angelica Gisselle Garcia Espindola
            #Alexis López Lira

######################################################

import json
Conocimiento = False
Sau = False
Mam = False
Vive = False

with open("info.json","r") as leer_archivo:
    data = json.load(leer_archivo)
    Conocimiento = data['conocimiento']
    Sau = data['sau']
    Mam = data['mam']
    Vive = data['vive']


# =================== FUNCION VIVE_EN() =========================

def vive_en(A, B):
    return vive(A, B, Vive)

def vive(A, B, CON):
    if not CON:
        return False
    
    Elemento = [e for e in CON if e[0] == A]

    if not Elemento:
        return False
    
    Elemento = Elemento[0]
    if Elemento[0] == "Tortuga" or Elemento[0] == "Cocodrilo":
        if Elemento[1] == B or Elemento[1] == "Tierra" or Elemento[1] == "Agua":
            return True
        else:
            return False
    
    if Elemento[1] == B:
        return True
    else:
        return False

# =============== FIN FUNCION VIVE() ===============



# ================ FUNCION TIENE() =============     
def tiene(A, B):
    return have(A, B, Conocimiento)

def have(A, B, CON):
    return es(A, B, CON)

# ================= FIN FUNCION TIENE() =================



# ================= FUNCION ES_UN() =========================

def es_un(A, B):
    return es(A, B, Conocimiento)

def es(A,B,CON):
    if not CON:
        return False
    Elemento = [e for e in CON if e[0] == A]
    if not Elemento:
        return False
    
    Elemento = Elemento[0]
    if Elemento[1] == B:
        return True
    valor = ""
    if Elemento[0] == "Tortuga" or Elemento[0] == "Gallo" or Elemento[0] == "Cocodrilo" or Elemento[0] == "Iguana":
        for i in Sau:
            if i == B:
                valor = i
        
        if valor != "":
            return True
        else:
            return False
    
    if Elemento[0] == "Gato" or Elemento[0] == "Ballena" or Elemento[0] == "Oso" or Elemento[0] == "Delfin":
        for i in Mam:
            if Elemento[0] == "Delfin" or Elemento[0] == "Ballena":
                if i == "Tetrapodo":
                    return False
            if i == B:
                valor = i
                break
        
        if valor != "":
            return True
        else:
            return False

def main():
    print("Escribe el nombre de las funciones que te interesen:")
    print('es_un( "Animal", " ¿que quieres saber?")')
    print('tiene( "Animal", " ¿que quieres saber?")')
    print('vive_en( "Animal", "Tierra/Agua")')
    print("Escribe 'q' o quit() para salir del programa")
    i = False
    while not i:
        Leer = input("> ")
        if Leer == 'q':
            return
        Evaluacion = eval(Leer)
        print(Evaluacion)


if __name__ == "__main__":
    main()