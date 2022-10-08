import threading
import time

PRODUCTOS_MAX = 5
PRODUCTORES = 3
CONSUMIDORES = 3


bodega = [] #Almacen de productos
mutex = threading.Lock() #Exclusión mutua al insertar o quitar elementos
semaf = threading.Semaphore(0) #Semaforo para bloquear consumidores
      
class Productor(threading.Thread):
  conta = 0
  
  def __init__(self):
    super(Productor, self).__init__()
    self.id  = Productor.conta
    Productor.conta += 1
  
  def productor(self):
    for i in range(PRODUCTOS_MAX):
      with mutex: #Con exclusión mutua:
        bodega.append(0) #Se inserta el producto a la bodega
        print("\nProductor num.", (self.id)," almacenó un producto")
        time.sleep(1)
      semaf.release()
      print("Productos en bodega:",len(bodega))
      
  def run(self):
    self.productor()
      
class Consumidor(threading.Thread):
  conta = 0
  
  def __init__(self):
    super(Consumidor, self).__init__()
    self.id  = Consumidor.conta
    Consumidor.conta += 1
  
  def consumidor(self):
    for i in range(PRODUCTOS_MAX):
      semaf.acquire()
      with mutex:
        bodega.pop(0)
        print("\nConsumidor num.", (self.id)," extrajo un producto") 
        time.sleep(1)
      print("Productos en bodega:",len(bodega))
  
  def run(self):
    self.consumidor()
  
def main():
    users = []

    for i in range(CONSUMIDORES):
      users.append(Consumidor())
      
    for i in range(PRODUCTORES):
      users.append(Productor())

    for t in users:
        t.start()

if __name__ == "__main__":
    main()