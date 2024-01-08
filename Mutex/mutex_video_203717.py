from threading import Thread
import threading
from time import sleep
import requests

mutex = threading.Lock()
guardar = "D:/Downloads/videosbonitos"
url = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ","https://www.youtube.com/watch?v=VZzSBv6tXMw&t=167s","https://www.youtube.com/watch?v=wAMZ6KpMGQI","https://www.youtube.com/watch?v=9bZkp7q19f0","https://www.youtube.com/watch?v=ZyhrYis509A","https://www.youtube.com/watch?v=kuqv4Cn2VAw","https://youtu.be/xGU-JTRdBRI","https://youtu.be/nv6FRU4_Tks","https://youtu.be/bwen5lsv23A","https://www.youtube.com/watch?v=Dz9OoMW-DP4"]


def crito(id):
    global x;
    global y;
    y=y+id;
    video = pytube.YouTube(url[x])
    video.streams.first().download(guardar)
    print("video "+ str(y) + " descargado")
    y=1
    x=x+1

class Hilo(threading.Thread):
    def __init__(self, id,url):
        threading.Thread.__init__(self)
        self.id=id
        self.url=url

    def run(self):
        mutex.acquire()
        crito(self.id,self.url)
        #print('valor ' + str(self.id))
        mutex.release()
    
hilos = [Hilo(1),Hilo(2),Hilo(3),Hilo(4),Hilo(5),Hilo(6),Hilo(7),Hilo(8),Hilo(9),Hilo(10)];
x=0;
y=0;

for h in hilos:
    h.start()