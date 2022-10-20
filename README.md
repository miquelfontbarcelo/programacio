# programacio
#llegir
#mirar si es nombre

#mostrar missatge de sí o no 

def llegirIP():
    print("escriu una ip")
    x = input()
    return x

def nombreValid(nombre):
    
    if (nombre >= 0) and (nombre <= 255):
        return True
    else:    
        return False

def comprovaIP(x):
    x = x.split(".")
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    d = int(x[3])
    if (nombreValid(a) and nombreValid(b) and nombreValid(c) and nombreValid(d)):
        print("es una ip vàlida. ",ip)
        return True
    else:
        print("és una ip NO vàlida. ", ip)
        return False
  

sortir = false
#llegir ip sencera (192.168.1.2)

while not sortir:
    ip = llegirIP()
    #la dividim en quatre parts(a=192,b=168,c=1,d=2)
    #comprovar tots els trossos amb nombreValid()
    if ip != 'sortir'
        comprovaIP(ip) 
    else:
        sortir = True
    #mostram que es vàlid
    #nombreValid(ip)

print ("Ha acabat l'execució")
