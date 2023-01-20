import socket
import json

# Declarar la dirección y el puerto del servidor UDP
UDP_IP = "localhost"
UDP_PORT = 3005

def process_data(pais):
    # Procesar los datos del país recibido
    print("País recibido:", pais)
    # Aquí puedes agregar cualquier otro código necesario para procesar los datos

# Crear un socket para recibir datos
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazar el socket al puerto
sock.bind((UDP_IP, UDP_PORT))

while True:
    # Recibir datos del servidor
    data, addr = sock.recvfrom(3005)

    # Descodificar los datos recibidos y convertirlos en un objeto país
    try:
        # Descodificar los datos recibidos y convertirlos en un objeto país
        pais = json.loads(data.decode())
    except json.decoder.JSONDecodeError:
        # Si los datos no son válidos, simplemente se ignoran
        continue

    # Procesar los datos recibidos
    process_data(pais)
