import requests
from pprint import pprint
import json
import psycopg2
def connect():
    conn = psycopg2.connect(host='localhost', user='postgres', password='Huevos1',  dbname='concurrente')
    return conn

def save_data(data):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('insert into pokemons(nombre) values(%s)', (data,))
    conn.commit()
    conn.close()

# Investigar sobre la libreria threading en python
#consumir un servicio que descargue por lo menos 5000 registros
def get_service():
	resp = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5000")
	if resp.status_code==200:
		resp_json =json.loads(resp.text)
		#pprint(resp_json["results"])
		for i in resp_json["results"]:
			
			nombre= i["name"]
			print(nombre)
			write_db(nombre)
	#write_db()
    #for x in data
		#write_db(x.name)
# Implementar requests
# Consumir un servicio que descarge por lo menos 5000 registros

def write_db(nombre):
	json_a_guardar = json.dumps(nombre)
	save_data(json_a_guardar)
# Escribir el response en una base de datos

if __name__ == "__main__":
	get_service()
	
	

	#instalar la extension liveshare
	#investigar threading