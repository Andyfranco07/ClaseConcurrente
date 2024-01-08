#Andy Omar Franco Bermudez
#203717
import threading
import concurrent.futures
from pprint import pprint
import json
import time
import pytube 
guardar = "D:/Downloads/videosbonitos"
url = ["https://www.youtube.com/watch?v=kuqv4Cn2VAw","https://youtu.be/xGU-JTRdBRI","https://youtu.be/nv6FRU4_Tks","https://youtu.be/bwen5lsv23A","https://www.youtube.com/watch?v=Dz9OoMW-DP4"]
threading_local = threading.local()

def get_service():
    for x in range(5):
        video0 = pytube.YouTube(url[x])
        video0.streams.first().download(guardar)

def servicio():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service)
        
if __name__ == "__main__":
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)
    
