from bs4 import BeautifulSoup
datos = {
    "Delhi": {
        "google": {
            "inicio": "164.52.192.1",
            "saltos": "8",
            "time": "9.79",
            "final": "142.250.206.142",
        },
        "youtube": {
            "inicio": "164.52.192.1",
            "saltos": "8",
            "time": "9.29",
            "final": "142.250.194.78",
        },
        "facebook": {
            "inicio": "164.52.192.1",
            "saltos": "9",
            "time": "15.11",
            "final": "157.240.1.35",
        }
    },
    "Tokio": {
        "google": {
            "inicio": "31.204.145.130",
            "saltos": "5",
            "time": "1.8",
            "final": "142.250.207.14",
        },
        "youtube": {
            "inicio": "31.204.145.131",
            "saltos": "4",
            "time": "2.25",
            "final": "52.223.34.187",
        },
        "facebook": {
            "inicio": "31.204.145.131",
            "saltos": "4",
            "time": "5.25",
            "final": "101.203.88.39",
        }
    },
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


#pais= ["Delhi","Tokio","Australia","Auckland","Amsterdam","Bruselas"]
#page= ["google","instagram","lidenking"]
#page= ["google","youtube","facebook"]
#page= ["google","docomo","yahoo"]
mapas="mapa_youtube_Asia.html"
pais=["Delhi","Tokio"]
page="youtube"
info=["inicio","saltos","time","final"]

# Leer el archivo HTML existente
with open(mapas, 'r') as file:
    html = file.read()

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar el elemento donde deseas agregar información
elemento = soup.find("body")#'div', {'id': 'mi_div'}

# Crear un nuevo elemento HTML
titulo=[]
txt=[]

for i in range(0,len(pais)):
    titulo.append(soup.new_tag('h3'))
    for i in range(0,len(info)):
        txt.append(soup.new_tag('p'))

titulo_t=tuple(titulo)
txt_t=tuple(txt)
j=0
i=0
for c in pais:
    titulo_t[j].string="\n"+c+" "+page+"\n"
    j=j+1
    for data in info:
        txt_t[i].string= "\n"+data+": "+datos[c][page][data]+"\n"
        i=i+1

# Agregar el nuevo elemento al elemento encontrado

elemento.append(titulo_t[0])
for i2 in range(0,len(info)):
    elemento.append(txt_t[i2])
    
elemento.append(titulo_t[1])
for i2 in range(len(info),len(info)*2):
    elemento.append(txt_t[i2])


# Escribir el archivo HTML actualizado
with open(mapas, 'w') as file:
    file.write(str(soup))
