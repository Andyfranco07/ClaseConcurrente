#Andy Omar Franco Bermúdez 203717
#Josue Benjamin Maldonado Urbina 203441 
import queue
import threading, time, random

espacio = queue.Queue(maxsize=20)
noOrden= queue.Queue()
mutexito = threading.Lock()
filaEspera = queue.Queue()
chefsitos= queue.Queue(maxsize=2)
class Coci(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.moni = threading.Condition()

    def quechille(self):
        while True:
            with self.moni:
                if not noOrden.empty():
                    if chefsitos.empty():
                        chefsitos.put(1)
                        print(f'Chefsito')
                        print(f'Estado: Cocinando')
                        time.sleep(3)
                        noOrden.get()
                        print(f'Orden')
                        print(f'Estado: Completada')
                        chefsitos.get()
                        finishOrden.put(1)
                        self.moni.notify()
                    else:
                        print(f'Chefsito')
                        print(f'Estado: Ocupados')
                        time.sleep(3)

    def run(self):
        self.quechille()

meserito = queue.Queue(maxsize=2)
class Mese(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.moni = threading.Condition()

    def meserear(self):
        while True:
            with self.moni:
                if espacio.qsize()>=1:
                    if meserito.empty():
                        meserito.put(1)
                        print(f'Mesero')
                        print(f'Estado: Recibiendo order')
                        time.sleep(3)
                        print(f'Orden')
                        print(f'Estado: Procesando')
                        noOrden.put(1)
                        meserito.get()
                        self.moni.notify()
                    else:
                        print(f'Mesero')
                        print(f'Estado: Ocupado')
                        time.sleep(2)
                else:
                    print(f'Mesero')
                    print(f'Estado: Descansando')
                    time.sleep(2)

    def run(self):
        self.meserear()

noReserva = queue.Queue(maxsize=4) 
class Reser(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.moni = threading.Condition()

    def reservar(self):
        print(f'Reservacion....')
        while True:
            with self.moni:
                if noReserva.qsize()<=4:
                    noReserva.put(self.id)
                    print(f'Numero de cliente: {self.id}')
                    print(f'Estado: Reserva lugar')
                    self.moni.notify()
                    time.sleep(5)
                else:
                    print(f'Numero de cliente: {self.id}')
                    print(f'Estado: En espera de lugar')
                    filaEspera.put(self.id)
                    time.sleep(5)
                self.id = self.id + 1

    def run(self):
        self.reservar()

finishOrden = queue.Queue()
class Aten(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.moni = threading.Condition()

    def empezar(self):
        print(f'Comer....')
        while True:
            with self.moni:
                if finishOrden.qsize() >=1:
                    noclien= espacio.get()
                    print(f'Numero de cliente: {noclien}')
                    print(f'Estado: Comiendo')

                    time.sleep(random.randint(4, 7))
                    print(f'Numero de cliente: {noclien}')
                    print(f'Estado: Termino')
                    noOrden.get()
                    self.moni.notify()
    def run(self):
        self.empezar()

class Recepcio(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.moni = threading.Condition()
        self.id = id

    def servicio(self):
        print(f'Su servicio....')
        while True:
            with self.moni:
                if noReserva.qsize() >=3:
                    espacio.put(self.id)
                    print(f'Numero de cliente: {self.id} ')
                    print(f'Atendido')
                    noReserva.get()
                    self.moni.notify() 
                else:
                    if filaEspera.empty():
                        if espacio.qsize() <=20:
                            espacio.put(self.id)
                            print(f'Numero de cliente: {self.id} ')
                            print(f'Atendido')
                            self.moni.notify()
                            time.sleep(3)
                        else:
                            filaEspera.put(self.id)
                            print(f'La fila es de: {filaEspera.qsize()}')
                            print(f'Tu numero es: {self.id} ')
                            time.sleep(3)
                    else:
                        print(f'Cliente {self.id} esta esperando')
                        filaEspera.put(self.id)
                        print(f'Hay {filaEspera.qsize()} clientes esperando')
                        time.sleep(3)
            self.id = self.id + 1

    def run(self):
        self.servicio()

if __name__ == '__main__':
    recep = Recepcio(1)
    recep.start()
    atender = Aten(1)
    atender.start()
    reserva = Reser(1)
    reserva.start()
    meseroo = Mese()
    meseroo.start()
    coci = Coci()
    coci.start()