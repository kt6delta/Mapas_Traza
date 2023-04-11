from scapy.all import *

# Definir el destino de la traza de ruta
destino = "sydneyoperahouse.com"

# Realizar la traza de ruta con un máximo de 30 saltos
respuestas, _ = traceroute(destino, maxttl=30)

# Imprimir la dirección IP de todos los saltos en la traza de ruta
for respuesta in respuestas:
    print(respuesta[0].src)


