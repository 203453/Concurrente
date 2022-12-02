
# Pasos para probar el juego

### 1.- Ejecutar archivo server.py
    De esta manera, tendremos el servidor corriendo mediante el cual la conexion de ambos jugadores se alojará.

### 2.- Abrir una nueva terminal y ejecutar client.py
    El objetivo de esto es cargar el juego y el cliente para que se una un jugador a la cola.

### 3.- Abrir de nuevo una terminal y ejecutar nuevamente client.py
Esto es para completar el emparejamiento y así tener a los dos jugadores en la cola para comenzar el juego.

### 4.- Presionar "Ready" en ambas ventanas del cliente
Esto cambiará a color verde al usuario indicando que está listo para iniciar el juego.

# Aspectos a tener en cuenta

### Errores con la IP
Puede existir un error de IP, la implementación de esto está hecho para reconocer la IP del equipo que ejecutará el juego, por lo que es lo adecuado para realizar las pruebas en una sola máquina, al usar dos máquinas, tendríamos que iniciar el servidor en la máquina que queramos pero la otra máquina en el código "server" tiene que ser igual a la IP de la máquina donde se ejecutará el server.py. (server es una variable usada para referirse a la IP donde se alojará el servidor)
