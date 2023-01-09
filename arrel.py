import math



print ("Escriu la sequència de naturals. Escriu 0 per acabar la llista:") 

#cream lllista buida

llista=[]

#cream un token per acabar
acabar = False
while (not acabar):
    #agafam el nombre a calcular
    nombre = int(input())
    if nombre ==0:
        acabar = True
    else:
        #El posam dins llista
        llista.append(nombre)
print(llista)  
for nombre in llista:
    txt= ("el nombre {} quadrat és {} i arell {:6f}")

    
    
""" 
while ( not acabar  ):
    nombre = int ( input("Nombre? ") )
    if ( nombre == 0 ):
        acabar = True
    else:
        #print(" El nombre al cuadrat és " + str( nombre*nombre ) + ". La arrel és " + str(math.sqrt( nombre )))
        txt= ("el nombre {} quadrat és {} i arell {:6f}")
        print(txt.format (nombre, nombre*nombre,math.sqrt(nombre)))

n = 15.00
print(f'{n:.6f}')
"""
