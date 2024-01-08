#CALLBACKS
# Es una devolucion de llamada es una funcion que se pasa como argumento donde se espera a que esta funcion
#llame a esta funcion de devolucion.
#Las funciones de devolucion de llamada se utilizan generalmente por funciones asincronas.
import  requests
import threading

def get_service_1(response_json_data):
    print(response_json_data)

def ger_error_1():
    print("error")

def get_service_1(response_json_data):
    print(response_json_data)

def get_error_1():
    print("error")

def requests_data():
    response = requests.get(url, success_callback, error_callback)
    
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()

class Hilo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        h1 = threading.Thread(target=requests_data, kwargs={
            'url':'',
            'success_callback':get_service_1,
            'error_callback':get_error_1
        })
        h1.start()
        h2 = threading.Thread(target=requests_data, kwargs={
            'url':'',
            'success_callback':get_service_2,
            'error_callback':get_error_2
        })
        h2.start()

hiloa=Hilo()
hiloa.start()