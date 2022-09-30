from random import randint
import threading
import time


palillos = []
uEating = []
uTotal = []
uN = 8

# Funcion para que el usuario tome los palillos
def catch(id):
    left_object = palillos[id]
    right_object = palillos[(id-1) % uN]
    
    left_object.acquire()
    
    if right_object.acquire():
        return True
    else:
        left_object.release()
        return False
    
# Se otorgan los palillos al usuario cercano en ese momento
def free(id):
    palillos[id].release()
    palillos[(id-1) % uN].release()
    print(f"El usuario {id} terminó de comer.")

# Funcion donde el usuario empieza a comer y los usuarios que estan en espera
def eating(id):
    
    if catch(id):
        print(f"\nEl usuario {id} empezó a comer")
        uEating.append(id)
        
        aux1 = set(uTotal).difference(set(uEating))
        aux2 = set(uEating).difference(set(uTotal))
        users_wating = list(aux1.union(aux2))

        if(users_wating == []):
            print("Usuarios en espera: Ninguno")
        else:
            print(f"Usuarios en espera: {users_wating}")
        
        time.sleep(randint(2,5))

        free(id)
            
if __name__ == '__main__':
    threads = []
    
    # Se agregan palillos al arreglo dependiendo la cantidad de personas
    for _ in range(uN):
        palillos.append(threading.Lock())
        
    for i in range(uN):
        uTotal.append(i)
        new_thread = threading.Thread(target=eating, args=(i,))
        threads.append(new_thread)
    
    # Se ejecuta la inicializacion de los hilos
    for hilo in threads:
        hilo.start()