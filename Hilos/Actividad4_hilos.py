#descargar 5 videos
#Escribir en base de datos por lo menos 2 mil registros
#generar una solicitud a random user de por lo menos 50 usuarios
#Andy Omar Franco Bermúdez
#203717
#IDS 7B
import requests 
import threading
import time
import concurrent.futures
from pprint import pprint
import psycopg2
import json
import pytube 

guardar = "D:/Downloads/videosbonitos"
url = ["https://www.youtube.com/watch?v=kuqv4Cn2VAw","https://youtu.be/xGU-JTRdBRI","https://youtu.be/nv6FRU4_Tks","https://youtu.be/bwen5lsv23A","https://www.youtube.com/watch?v=Dz9OoMW-DP4"]
threading_local = threading.local()

def get_nombre():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
       results = response.json().get('results')
       name = results[0].get('name').get('first')
       print(name)

#video
def descargar():
    for x in range(5):
        video0 = pytube.YouTube(url[x])
        video0.streams.first().download(guardar)
        y=x+1
        print("video", y , "descargado")


 #base de datos       
def connect():
    conn = psycopg2.connect(host='localhost', user='postgres', password='Huevos1',  dbname='concurrente')
    return conn

def save_data(data):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('insert into pokemons(nombre) values(%s)', (data,))
    conn.commit()
    conn.close()

def get_pokeapi():
	resp = requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000")
	if resp.status_code==200:
		resp_json =json.loads(resp.text)
		#pprint(resp_json["results"])
		for i in resp_json["results"]:
			nombre= i["name"]
			#print(nombre)
			write_db(nombre)

def write_db(nombre):
	json_a_guardar = json.dumps(nombre)
	save_data(json_a_guardar)

if __name__ == "__main__":
    init_time = time.time()
    th2 =threading.Thread(target=descargar)
    th2.start()
    th2.join()
    th3 =threading.Thread(target=get_pokeapi)
    th3.start()
    for x in range(0,50):
        th1 =threading.Thread(target=get_nombre)
        th1.start()
        th1.join()
    end_time = time.time() - init_time
    print(end_time)
    