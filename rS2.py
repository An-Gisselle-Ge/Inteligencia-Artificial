import json
Conocimiento = False

with open("rS2.json","r") as read_file:
    data = json.load(read_file)
    Conocimiento = data['conocimiento']

def es(A,B):
    return es_(A,B, Conocimiento)
def es_(A,B,CON):
    if not CON:
        return False
    
    Elemento = [e for e in CON if e[0] == A]

    if not Elemento:
        return False
    
    Elemento = [e for e in Elemento if e[1] == 'es']
    Elemento = [e for e in Elemento if e[2] == B ]
    if not Elemento:
        return False
    else:
        return True

def tiene(A,B):
    return tiene_(A,B,Conocimiento)

def tiene_(A,B,CON):
    if not CON:
        return False
    
    Elemento = [e for e in CON if e[0] == A]

    if not Elemento:
        return False
    
    Elemento = [e for e in Elemento if e[1] == 'tiene']
    Elemento = [e for e in Elemento if e[2] == B ]
    if not Elemento:
        return False
    else:
        return True


def vive(A,B):
    return vive_(A,B, Conocimiento)
def vive_(A,B,CON):
    if not CON:
        return False
    
    Elemento = [e for e in CON if e[0] == A]

    if not Elemento:
        return False
    
    Elemento = [e for e in Elemento if e[1] == 'vive']
    Elemento = [e for e in Elemento if e[2] == B ]
    if not Elemento:
        return False
    else:
        return True


def main():
    print("Escribe el nombre de las funciones que te interesen:")
    print('es( "Animal", " ¿que quieres saber?")')
    print('tiene("Animal", " ¿que quieres saber?")')
    print('vive( "Animal", "Tierra/Agua")')
    print("Escribe 'q' o quit() para salir del programa")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if Leer == "q":
            return
        Imprimir = eval(Leer)
        print(Imprimir)


if __name__ == "__main__":
    main()