from bs4 import BeautifulSoup
datos = {
    "Australia": {
        "google": {
            "inicio": "221.121.154.216",
            "saltos": "11",
            "time": "2.118",
            "final": "142.250.66.228",
        },
        "instagram": {
            "inicio": "221.121.154.216",
            "saltos": "10",
            "time": "3.97",
            "final": "157.240.8.174",
        },
        "lidenking": {
            "inicio": "221.121.154.216",
            "saltos": "15",
            "time": "3.68",
            "final": "13.107.42.14",
        }
    },
    "Auckland": {
        "google": {
            "inicio": "49.50.246.153",
            "saltos": "10",
            "time": "18.06",
            "final": "172.217.24.36",
        },
        "instagram": {
            "inicio": "49.50.246.153",
            "saltos": "11",
            "time": "3.48",
            "final": "31.13.78.174",
        },
        "lidenking": {
            "inicio": "49.50.246.153",
            "saltos": "7",
            "time": "3.52",
            "final": "13.107.42.14",
        }
    },
    "Amsterdam": {
        "google": {
            "inicio": "5.79.88.28",
            "saltos": "13",
            "time": "6.16",
            "final": "142.250.184.228",
        },
        "instagram": {
            "inicio": "5.79.88.28",
            "saltos": "10",
            "time": "6.91",
            "final": "157.240.20.174",
        },
        "lidenking": {
            "inicio": "5.79.88.28",
            "saltos": "8",
            "time": "1.76",
            "final": "13.107.42.14"
        }
    },
    "Bruselas": {
        "google": {
            "inicio": "91.207.57.97",
            "saltos": "13",
            "time": "150.64",
            "final": "142.250.179.132",
        },
        "instagram": {
            "inicio": "91.207.57.97",
            "saltos": "9",
            "time": "11.17",
            "final": "157.240.252.174",
        },
        "lidenking": {
            "inicio": "91.207.57.97",
            "saltos": "9",
            "time": "109.93",
            "final": "13.107.42.14",
        }
    }
}


# Leer el archivo HTML existente
with open('archivo.html', 'r') as file:
    html = file.read()

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar el elemento donde deseas agregar información
elemento = soup.find('div', {'id': 'mi_div'})

# Crear un nuevo elemento HTML
nuevo_elemento = soup.new_tag('p')
nuevo_elemento.string = 'Nueva información desde Python'

# Agregar el nuevo elemento al elemento encontrado
elemento.append(nuevo_elemento)

# Escribir el archivo HTML actualizado
with open('archivo.html', 'w') as file:
    file.write(str(soup))
