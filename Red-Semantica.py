#Garcia Espindola Angelica Gisselle
#Lopez Lira Alexis

conocimiento = [
    ("Tortuga", "Souropsido"),
    ("Gallo", "Souropsido"),
    ("Cocodrilo", "Souropsido"),
    ("Iguana", "Souropsido"),
    ("Gato", "Mammalia"),
    ("Ballena", "Mammalia"),
    ("Oso", "Mammalia"),
    ("Delfin","Mammalia"),
]
SAU = [
    "Proteccion Queratina",
    "Garras",
    "Vertebrado",
    "Oviparo",
    "Tetrapodo"
]
MAM = [
    "Viviparo",
    "Glandulas Mamarias",
    "Vertebrado",
    "Pelo",
    "Tetrapodo"
]

VIVE = [
    ("Tortuga", "Agua" ),
    ("Gallo", "Tierra"),
    ("Cocodrilo", "Agua"),
    ("Iguana", "Tierra"),
    ("Gato", "Tierra"),
    ("Ballena","Agua"),
    ("Oso", "Tierra"),
    ("Delfin", "Agua")
]


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
        
def tiene(A, B, CON):
    return es(A, B, CON)
    
    


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
        for i in SAU:
            if i == B:
                valor = i
        
        if valor != "":
            return True
        else:
            return False
    
    if Elemento[0] == "Gato" or Elemento[0] == "Ballena" or Elemento[0] == "Oso" or Elemento[0] == "Delfin":
        for i in MAM:
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
    

print(es("Delfin", "Tetrapodo", conocimiento))
print(tiene("Gallo", "Pelo", conocimiento))
print(vive("Tortuga", "Agua", VIVE))
#Una tortuga tambien puede ser de tierra
print(vive("Tortuga", "Tierra", VIVE))
print(vive("Cocodrilo", "Tierra", VIVE))
# Cocodrilo puede vivir en tierra
print(vive("Cocodrilo", "Agua", VIVE))
