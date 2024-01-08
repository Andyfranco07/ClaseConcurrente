import queue
import threading
import time

threading_cond = threading.Condition()
bodegita = queue.Queue(10)


if __name__ == '__main__':
    for x in range(10):
        consumidores = consumidores(x)
        consumidores.start()
        productores = Productores(x)
        productores.start()

class Consumidores(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        global bodegita;
        while True:
            threading_cond.acquire()
            threading_cond.wait()
            if bodegita.full():
                while bodegita.qsize() != 0:                    
                    print(f'Consumidor {self.id}')
                    print(f'Consume {bodegita.get()}')
                    time.sleep(1)
                    bodegita.get()
            threading_cond.notify()
            threading_cond.release()

class Productores(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        global bodegita;
        while True:
            threading_cond.acquire()
            if bodegita.full():
                print(f'Productor {self.id} No')
                cond.wait()
            threading_cond.put(1)
            print(f'Productor {self.id} Yes')
            time.sleep(1.5)
            threading_cond.notify()
            threading_cond.release()