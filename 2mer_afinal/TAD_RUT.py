from sys import stdin
class lista(object):
    """esta funcion crea dos diccionarios vacios, uno guarda las conecciones
que existen entre las ciudades, el otro guarda todo los datos enteros en esa
posicion del diccionario"""
    def __init__(self):
        #conecciones de ciudades
        self.dic_conecciones={}
        #indices-ciudad
        self.dic_indices={}
        #ciudad-indices
        self.dic_ciud={}
        
        self.dic_dat={}
        self.con=0
        #guarda todas las rutas
        self.dic_rec={}
        #guarda un recorrido una vez y si llega al destino se reinicia
        self.ruta=[]
        #guarda los peajes en la misma posicion de las conecciones
        self.dic_peajes={}
        #guarda un recorrido de peajes a la vez, si llega al destino se reinicia
        self.peajes=[]
       
    """esta funcion hace la lectura de los datos, las ciudades
    las guarda en un diccionario, con sus respectivos datos, las ciudades dejan
    de tener un nombre, ahora tienen un numero en el diccionario"""
    def lec(self,dat):
        self.dic_dat[self.con]=dat
        self.con+=1
        
    """esta funcion imprime todos los datos en un diccionario"""
    def pdatos(self):
        return self.dic_dat
    
    """esta funcion imprime los indices de todas las ciudades en un diccionario"""
    def pindices(self):
        return self.dic_indices
    
    """esta funcion guarda los indices de cada ciudad en un diccionario"""
    def indices(self,num,ciudad):
        if len(self.dic_indices)==0:
           self.dic_indices[num]=ciudad
           self.dic_ciud[ciudad[1]]=ciudad[0]
           return False
        
        else:
            bol=False
            
            for x in range(max(self.dic_indices)+1):
                conjunto=self.dic_indices[x]
                if ciudad[1]== conjunto[1]:
                    bol=True
                    break
                
            if bol==True :               
                return True
            
            else:
                self.dic_indices[ciudad[0]]=ciudad
                self.dic_ciud[ciudad[1]]=ciudad[0]
                return False
        
    """esta funcion hace las conecciones de cuales ciudades estan conectadas con cuales, las guarda en el constructor
    tambien guarda los peajes en su diccionario respectivo, en el mismo orden"""
    def conecciones(self,origen,destino,peajes):
        pepe=self.dic_indices[0]
        origeni=0
        destinoi=0
        bol1=0
        bol2=0
        for x in range(0,max(self.dic_indices)+1):
            indic_ciud=self.dic_indices[x]
            if origen == indic_ciud[1] and bol1!=1:
                origeni=indic_ciud[0]
                
        
            if destino== indic_ciud[1] and bol2!=1:
                destinoi=indic_ciud[0]
                bol2=1
                
        if len(self.dic_conecciones)==0 :
                self.dic_conecciones[origeni]=[origeni,destinoi]
                self.dic_peajes[origeni]=[origeni,peajes]
                return
        try:
            self.dic_conecciones[origeni].append(destinoi)
            self.dic_peajes[origeni].append(peajes)
            return
        except:
                self.dic_conecciones[origeni]=[origeni,destinoi]
                self.dic_peajes[origeni]=[origeni,peajes]
                return
            
    """este metodo imprime el diccionario de peajes""" 
    def ppeajes(self):
        return self.dic_peajes
    """este metodo imprime el diccionario de conecciones"""   
    def pconecciones(self):
        return self.dic_conecciones
    """este metodo imprime el diccionario de ciudaes a indices"""
    def pciud(self):
        return self.dic_ciud
    
    """esta funcion realiza la busqueda de origen, destino, la cual es llamada por la funcion recorridos, nunca
    retorna porque va guardando en los constructores de peajes y recorridos, se va actualizando"""
    def buscar(self,x,lleg,viajes,peajes,part):
        if x in self.dic_conecciones:
            mogadicio=False
            for y in self.dic_conecciones[x]:
                if int(y)== int(lleg):
                    if y != viajes[-1]:
                        ind=self.dic_conecciones[x].index(y)                        
                        peajin=self.dic_peajes[x][ind]
                        peajes.append(peajin)                                     
                        viajes.append(y)
            
                    if len(self.ruta)>0 and viajes[-1]==lleg:
                        mogadicio=True
                        try:
                            self.dic_rec[len(self.ruta)].append([tuple(self.ruta),(sum(peajes))])
                            
                           
                        except:
                             self.dic_rec[len(self.ruta)]=[[tuple(self.ruta),(sum(peajes))]]
                             
                        viajes.remove(viajes[-1])
                        peajes.remove(peajes[-1])
                if mogadicio==False or (mogadicio == True and x!=lleg and len(viajes)>1) :
                    if y in self.dic_conecciones[x] and y!=x and y!=lleg:
                        
                        if x ==part and y not in self.dic_conecciones[x] or x ==lleg and len(viajes)==1:
                            print("falla?")                                                  
                            nada=0
                        elif y in self.dic_conecciones and y not in viajes:
                            ind=self.dic_conecciones[x].index(y)
                            peajin=self.dic_peajes[x][ind]
                            peajes.append(peajin)
                            viajes.append(y)
                            self.buscar(y,lleg,viajes,peajes,part)
                            viajes.remove(viajes[-1])
                            peajes.remove(peajin)
                            #o si no es peajes.remove(peajes[-1])
                                
    """esta funcion verifica que se parta de la ciudad inicial, llama a la funcion busqueda"""
    def recorridos(self,partida,llegada):
        "pini: peaje inicial"
        try:
            part=self.dic_ciud[partida]
            lleg=self.dic_ciud[llegada]
        except:
            return False
    
        self.ruta=[part]
        
        for x in self.dic_conecciones:            
            if self.dic_conecciones[x][0]==part:
                
                if x not in self.ruta or len(self.ruta)==1:
                    
                    cont=0
                    for y in self.dic_conecciones[x]:
                        if y != self.dic_conecciones[x][0]:
                            p=self.dic_peajes[x][cont]
                            self.peajes.append(p)
                            self.ruta.append(y)
                            viajes=(self.ruta)
                            peajes=self.peajes
                            c=self.buscar(y,lleg,viajes,peajes,part)
                            
                        if len(self.ruta)>0 and self.ruta[-1] == lleg:
                             
                            try:
                                
                                if tuple(self.ruta) not in self.dic_rec[len(self.ruta)] :
                                    self.dic_rec[len(self.ruta)].append([tuple(self.ruta),sum(peajes)])
                                
                            except:
                                    self.dic_rec[len(self.ruta)]=[[tuple(self.ruta),sum(peajes)]]
            
                        cont+=1
                        self.ruta=[part]
                        self.peajes=[]
            
            
       
        if len (self.dic_rec)!= 0:
            print("RUTAS POSIBLES: ",self.dic_rec)
            print("__________")
            print()
            return True
        else:
            return False


        
"""Ibagué,cali,191,3.11,4
bogota,Ibagué,191,3.11,4
bogota,cali
Ibagué,putumayo
putumayo,bogota"""
"""1
bogota,cartagena,1,1,1
cartagena,barranquilla,6,1,5
bogota,medellin,2,1,3
medellin,bogota,0,1,8
barranquilla,medellin,0,1,4
cipa,medellin,0,1,3
medellin,san,3,1,20
bogota,san,50,50,50
medellin,alf,0,1,7
alf,asd,1,1,0
asd,san,2,1,1

///estos no
bogota,rumi
rumi,none

bogota
san
    
    Mayor recorrido de 7 viaje:  bogota -> cartagena -> barranquilla -> medellin -> alf -> asd -> san

    Menor distancia: 5.0 viaje: bogota -> medellin -> san

    Menor tiempo: 2.0 viaje: bogota -> medellin -> san

    Menos peajes: 11.0 viaje: bogota -> medellin -> alf -> asd -> san
    
Arauca,Mocoa,14,1283
Arauca,Bucaramanga,1,420
Arauca,Bogota,3,633
Barranquilla,Medellin,19,702
Barranquilla,Santa Marta,2,105
Santa Marta,Barranquilla,1,100
Barranquilla,Mompox,0,355
Bogota,Tunja,3,152
Bogota,Arauca,7,633
Paipa,Bogota,3,191
Cartagena,Barranquilla,3,120
Cali,Popayan,2,138
Bucaramanga,San Alberto,4,550
Tunja,San Alberto,8,800
San Alberto,Tunja,5,800
Tunja,Bucaramanga,4,283
Bucaramanga,Tunja,5,283
Medellin,Barranquilla,21,702
Mompox,Cartagena,1,317
Barranquilla,Cartagena,3,120
Medellin,Manizales,2,192
Manizales,Medellin,3,194
Cali,Toribio,0,92
Valledupar,Barranquilla,5,295
San Alberto,Valledupar,3,110
Valledupar,San Alberto,3,110
San Alberto,Mompox,0,180
San Alberto,Medellin,1,300
Manizales,Bogota,4,302
Bogota,Neiva,5,292
Neiva,Mocoa,2,321
Mocoa,Cali,2,411
Pasto,Mocoa,6,147
Popayan,Pasto,2,252
Pasto,Popayan,1,249
Bogota,Cali,10,464
Cali,Bogota,10,464
"""
        
        
"""esta funcion genera las conecciones que hay entre ciudades
    origeni=indice del origen
    desinoi=indice del destino
if p:
        print("EL MAYOR NUMERO DE CIUDADES A RECORRER ES: ",(max(dat.dic_rec),(nombres(dat,False,None)))
        
        print(minimo(dat),"tiene menor numero de peajes")"""
""" partida=input("Ingrese Partida: ").strip()
    partida=partida[0].upper()+partida[1:].lower()
    llegada=input("Ingrese Destino: ").strip()
    llegada=llegada[0].upper()+llegada[1:].lower()"""
