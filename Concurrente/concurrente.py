#Andy omar Franco Bermúdez
#203717
#IDS 7B
import requests
from pprint import pprint
import json
import time
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

def get_service():
	resp = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5000")
	if resp.status_code==200:
		resp_json =json.loads(resp.text)
		#pprint(resp_json["results"])
		for i in resp_json["results"]:
			nombre= i["name"]
			print(nombre)
			write_db(nombre)

def write_db(nombre):
	json_a_guardar = json.dumps(nombre)
	save_data(json_a_guardar)

if __name__ == "__main__":
	init_time = time.time()
	get_service()
	end_time = time.time() - init_time
	print(end_time)