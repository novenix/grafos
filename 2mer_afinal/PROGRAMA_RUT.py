from sys import stdin
from TAD_RUT import *
def minimo(dat):
    cont=False
    actual=0
    llave=0
    pepe=0
    for x in dat.dic_rec:
        #print(dat.dic_rec[x])
        for y in range(len(dat.dic_rec[x])):
            compara=dat.dic_rec[x][y][1]

            if compara < actual or cont== False:
                actual=compara
                pepe=dat.dic_rec[x][y]
                cont=True
                
    pepe=nombres(dat,True,pepe[0])
    return pepe,actual
            
def nombres(dat,boolean,lista):
    pepe=[]
    if boolean ==True:
       for x in lista:
        for y in dat.dic_indices:
            if x == dat.dic_indices[y][0]:
                pepe.append(dat.dic_indices[y][1])
    else:
        pepe=[]
        for x in dat.dic_rec[max(dat.dic_rec)][0][0]:
            for y in dat.dic_indices:
                if x == dat.dic_indices[y][0]:
                    pepe.append(dat.dic_indices[y][1])
    print("_________________________")
    print()
    return pepe
"""esta funcion hace la lectura de todos los datos, y llama la funcion connecciones, para guardar las conecciones respectivas"""

def rutas(dat,datos):
    for x in range(len(datos)):
        info=datos[x]
        origen=info[0]
        destino=info[1]

        #print(info)
        peajes=int(info[2])
        dat.conecciones(origen,destino,peajes)
    print()

    print(dat.pconecciones())
    print(dat.ppeajes())
    print(dat.pindices())
    
    print(dat.pciud())
    print("____________________________________")
    print()
"""funcion principal:
lee y convierte los datos en numeros para manejar todas las ciudades numericamente"""
def main():
    dato=stdin.readline().strip().split(",")
    dat=lista()
    
    while len(dato) != 1 :
        dat.lec(dato)
        dato=stdin.readline().strip().split(",")
        #print(dato,"1",(len(dato)))
        if len(dato)!=1 and dato !="":
            
            dato[0]=dato[0].lower()
            
            dato[1]=dato[1].lower()
            #print(dato)
            
    partida=input("Ingrese Partida: ").strip().lower()
    
    llegada=input("Ingrese Destino: ").strip().lower()
    
    datos=dat.pdatos()
    #print(datos,"datos")
    cont=0
    for x in range(len(datos)):
        num=datos[x]
        ciudad=[cont,num[0]]
        pepe=dat.indices(x,ciudad)
        if pepe==False:
            cont+=1
    pepe=False
    for x in range(len(datos)):
        num=datos[x]
        ciudad=[cont,num[1]]
        pepe=dat.indices(x,ciudad)
        if pepe ==False:
            cont+=1
    print("____________________________________________________________________")
    rutas(dat,datos)
    
    p=dat.recorridos(partida,llegada)
    
    if p:
        print(p)
        print("EL MAYOR NUMERO DE CIUDADES A RECORRER ES: ",nombres(dat,False,None),"con",(max(dat.dic_rec)))
        mini,peaj=minimo(dat)
        print("LA RUTA:",mini,"tiene el menor numero de peajes con",peaj)
    else:
       print(p,"LA RUTA DE",partida,"HACIA",llegada,"no existe!")
    """if p:
        print("EL MAYOR NUMERO DE CIUDADES A RECORRER ES: ",max(dat.dic_rec),(dat.dic_rec[max(dat.dic_rec)]))
        print(max(dat.dic_rec),(nombres(dat,False,None)))
        print(minimo(dat),"tiene menor numero de peajes")"""
    
main()
