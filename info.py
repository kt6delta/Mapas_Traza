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
with open('mapa_facebook_Asia.html', 'r') as file:
    html = file.read()

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar el elemento donde deseas agregar información
elemento = soup.find("body")#'div', {'id': 'mi_div'}

# Crear un nuevo elemento HTML

pais= ["Australia","Auckland","Amsterdam","Bruselas"]
page= ["google","instagram","lidenking"]
titulo=[]
txt=[]

titulo.apend( soup.new_tag('h3'))
titulo.string ="\n"+pais+page+"\n"
txt.append(soup.new_tag('p'))
google1 .string = "\ninicio: "+datos[pais][page]["inicio"]+"\n"
txt.append(soup.new_tag('p'))
google2.string = "\nsaltos: "+datos[pais][page]["saltos"]+"\n"
txt.append(soup.new_tag('p'))
google3.string = "\ntime: "+datos[pais][page]["time"]+"\n"
txt.append(soup.new_tag('p'))
google4.string = "\nfinal: "+datos[pais][page]["final"]+"\n"


# Agregar el nuevo elemento al elemento encontrado
elemento.append(titulo1)
elemento.append(google1)
elemento.append(google2)
elemento.append(google3)
elemento.append(google4)


# Escribir el archivo HTML actualizado
with open('mapa_facebook_Asia.html', 'w') as file:
    file.write(str(soup))
