#Crear una aplicacion en la cual descargaran 10 recursos diferentes integrando el concepto de semaforizacion
import requests 
import threading
import concurrent.futures
from pprint import pprint
import psycopg2
import json
import pytube
from threading import Thread, Semaphore

guardar = "D:/Downloads/videosbonitos"
url = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ","https://www.youtube.com/watch?v=VZzSBv6tXMw&t=167s","https://www.youtube.com/watch?v=wAMZ6KpMGQI","https://www.youtube.com/watch?v=9bZkp7q19f0","https://www.youtube.com/watch?v=ZyhrYis509A","https://www.youtube.com/watch?v=kuqv4Cn2VAw","https://youtu.be/xGU-JTRdBRI","https://youtu.be/nv6FRU4_Tks","https://youtu.be/bwen5lsv23A","https://www.youtube.com/watch?v=Dz9OoMW-DP4"]
semaforo = Semaphore(1)

def descargar(id):
    global x;
    global y;
    y=y+id;
    video = pytube.YouTube(url[x])
    video.streams.first().download(guardar)
    print("video "+ str(y) + " descargado")
    y=1
    x=x+1

def region_critica(id):
    global x;
    x=x+id;
    print ("El hilo"+str(id)+" valor de x="+str(x));
    x=1;
    

class Hilo(Thread):
    def __init__(self,id): #Constructor de la clase
         Thread.__init__(self);
         self.id=id;
 
    def run(self): #Metodo que se ejecutara con la llamada start
          semaforo.acquire();
          descargar(self.id);
          semaforo.release();

hilos = [Hilo(1),Hilo(2),Hilo(3),Hilo(4),Hilo(5),Hilo(6),Hilo(7),Hilo(8),Hilo(9),Hilo(10)]; #Creacion de objetos Hilos
x=0;
y=0;
for h in hilos: 
     h.start();
