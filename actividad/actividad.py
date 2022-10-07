import threading
import time

PRODUCTOS_MAX = 5
PRODUCTORES = 3
CONSUMIDORES = 3
PRODUCTO_INIT = 0

bodega = [] #Almacen de productos
mutex = threading.Lock() #Exclusión mutua al insertar o quitar elementos
notEmpty = threading.Semaphore(0) #Semaforo para bloquear consumidores
      
class Productor(threading.Thread):
  conta = 0
  
  def __init__(self):
    super(Productor, self).__init__()
    self.id  = Productor.conta
    Productor.conta += 1
  
  def productor(self):
    global PRODUCTO_INIT
    for i in range(PRODUCTOS_MAX):
      with mutex: #Con exclusión mutua:
            bodega.append(PRODUCTO_INIT) #Se inserta el producto a la bodega
            PRODUCTO_INIT += 1
            print("\nProductor num.", (self.id)," almacenó un producto")
            time.sleep(1)
      notEmpty.release()
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
    global PRODUCTO_INIT
    for i in range(PRODUCTOS_MAX):
      notEmpty.acquire()
      with mutex:
        aux = bodega.pop(0)
        print("\nConsumidor num.", (self.id)," extrajo un producto") 
        PRODUCTO_INIT += 1
        time.sleep(1)
      print("Productos en bodega:",len(bodega))
  
  def run(self):
    self.consumidor()
  
def main():
    personas = []

    for i in range(CONSUMIDORES):
      personas.append(Consumidor())
      
    for i in range(PRODUCTORES):
      personas.append(Productor())

    for t in personas:
        t.start()

if __name__ == "__main__":
    main()