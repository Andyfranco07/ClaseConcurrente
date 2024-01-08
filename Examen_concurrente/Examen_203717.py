import threading
import time

mutex = threading.Lock()

class Hilo(threading.Thread):
    def __init__ (self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run (self):
        mutex.acquire()
        comiendo(self.id)
        mutex.release()

def comiendo(id):
    while True:
        comiendo = pali(id)
        impri= id+1
        if comiendo ==True:
            print("-----------------------")
            print("Persona "+str(impri)+" comiendo\n")
            if impri+1!=9:
                print("Persona "+str(impri+1)+" en espera\n")
            time.sleep(3)
            print("Persona "+str(impri)+" acabo\n")
            time.sleep(3)
            veri_pali(id)
            break

def pali(id):
    palillo_izq = palillo_personas[id]
    palillo_der = palillo_personas[id-1]

    palillo_izq.acquire()

    if palillo_der.acquire(blocking=False):
        return True
    else:
        palillo_izq.release()
        return False

def veri_pali(id):
    palillo_personas[id].release()
    palillo_personas[(id - 1)].release()

palillo_personas=[threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock()]
if __name__=="__main__":
    for x in range(8):
        persona=Hilo(x)
        persona.start()