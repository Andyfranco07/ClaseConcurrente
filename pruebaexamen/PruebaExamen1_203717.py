import threading
import time
from threading import Thread
import requests


verificacion = True
urles=["https://disneylatino.com/","https://www.planetadelibros.com/editorial/planeta-comic/54","https://www.dcshoes.es/","https://www.marvel.com/","https://www.kelloggs.es/es_ES/brands/kellogg-s-corn-flakes-consumer-brand.html","https://www.instagram.com/","https://magic.wizards.com/es","https://www.pokemon.com/el/","https://www.adultswim.com/","https://www.minecraft.net/es-es","https://store.steampowered.com/?l=spanish","https://www.epicgames.com/site/es-ES/home","https://www.opera.com/es","https://vetealaversh.com/","https://www.upchiapas.edu.mx/","https://www.amazon.com.mx/","https://docs.google.com/document/u/0/?hl=es&tgif=d","https://monkeytype.com/","https://www.riotgames.com/es","https://www.twitch.tv/","https://es.xhamster.com/","https://www.google.com/","https://www.flightradar24.com/39.62,-103.61/4","https://www.youtube.com/","https://twitter.com/?lang=es","https://www.howmanypeopleareinspacerightnow.com/"]
    

def tiempo(id,urle):
    r = requests.head(urle)
    if r.status_code==200:
        print("link activado")
        verificacion = True
    else:
        print("link desactivado")
        verificacion= False
    print("status: "+ str(r)+urle)      


class Hilo(threading.Thread):
    def __init__(self, id,url):
        threading.Thread.__init__(self)
        self.id=id
        self.url=url

    def run(self):
        tiempo(self.id,self.url)

x=0
y=1

while(verificacion==True):
    for j in urles:
        h= Hilo(y,j)
        h.start()
        y=y+1
    y=1

    time.sleep(240)