import folium


def CreaTraza(page, posicion, color, id, peso, map):
    o = [(posicion[page[ip]]['y'], posicion[page[ip]]['x'])
         for ip in page]
    d = [(posicion[page[ip]]['y'], posicion[page[ip]]['x'])
         for ip in list(page.keys())[1:]]
    c = [page[ip] for ip in page]
    i = 0

    for ip in list(page.keys()):
        name = c[i]
        o_lat, o_lon = o[i]
        folium.Marker(location=[o_lat, o_lon],
                      popup=name+" ip:"+ip).add_to(map)
        if i < len(d):
            d_lat, d_lon = d[i]
            folium.Marker(location=[d_lat, d_lon],
                          popup=name+" ip:"+ip).add_to(map)
            folium.PolyLine(locations=[(o_lat, o_lon), (d_lat, d_lon)],
                            tooltip=f'{id}', color=color, weight=peso).add_to(map)
            i += 1


def Amsterdam(m_g, m_i, m_l):
    # Europa del Norte: Amsterdam, Holanda
    posicion = {
        "Haarlem": {"y": 52.3824, "x":  4.8995},
        "Cheney": {"y": 37.751, "x": - 97.822},
        "Cassel": {"y": 51.2993, "x": 9.491},
        "Dublin": {"y": 53.3472, "x": - 6.2439},
        "Francfort": {"y": 50.1188, "x":	8.6843},
        "Amsterdam": {"y": 52.2973, "x": 4.7946},
        "": {"y": 52.3824, "x": 4.8995},
    }
    google = {
        "5.79.88.28": "Haarlem",
        "142.250.184.228": "Cheney"
    }
    instagram = {
        "5.79.88.28": "Haarlem",
        "80.81.194.40": "Cassel",
        "31.13.26.112": "Dublin",
        "157.240.39.175": "Cheney",
        "157.240.20.174": "Francfort",
    }
    lidenking = {
        "5.79.88.29": "Haarlem",
        "81.17.33.136": "",
        "80.249.209.21": "Amsterdam",
        "104.44.239.81": "Cheney",
        "13.104.185.177": "Amsterdam",
        "13.107.42.14": "Cheney",
    }
    CreaTraza(google, posicion, 'green', "google: Amsterdam, Holanda", 2, m_g)
    CreaTraza(instagram, posicion, 'red',
              "instagram, Amsterdam, Holanda", 2, m_i)
    CreaTraza(lidenking, posicion, 'blue',
              "lidenking, Amsterdam, Holanda", 2, m_l)


def Bruselas(m_g, m_i, m_l):
    # Europa del Norte: Bruselas, Bélgica
    posicion = {
        "Bruselas": {'y': 50.8847, 'x': 4.5049},
        "Sofía": {'y': 42.6951, 'x': 23.325},
        "Lovnic": {'y': 45.9968, 'x': 24.997},
        "Austin": {'y': 30.2887, 'x': - 97.7398},
        "Cheney": {'y': 37.751, 'x': -97.822},
        "Detroit": {'y': 42.5138, 'x': - 82.9396},
        "Dublin": {'y': 53.3472, 'x': -6.2439},
        "Francfort": {'y': 50.1188, 'x': 8.6843},
        "": {'y': 1.3673, 'x': 103.8014},
        "Barcelona": {'y': 41.387, 'x': 	2.1701},
        "Amsterdam": {'y': 52.2973, 'x': 4.7946},
        "Düsseldorf": {'y': 51.2184, 'x':6.7734},
    }
    google = {
        "91.207.57.97": "Bruselas",
        "193.9.115.185": "Sofía",
        "212.103.51.87": "Lovnic",
        "72.14.239.217": "Austin",
        "108.170.251.208": "Cheney",
        "142.250.179.132": "Detroit"
    }
    instagram = {
        "91.207.57.97":	"Bruselas",
        "193.9.115.185": "Sofía",
        "193.27.15.254": "Lovnic",
        "103.4.99.24": "",
        "31.13.28.32": "Dublin",
        "157.240.34.239": "Cheney",
        "157.240.252.174": "Francfort"
    }
    lidenking = {
        "91.207.57.97":	"Bruselas",
        "193.9.115.185": 	"Sofía",
        "146.70.1.222":   "Lovnic",
        "37.120.220.105": "Barcelona",
        "80.249.209.20": "Amsterdam",
        "104.44.230.44": "Cheney",
        "13.104.185.208": "Düsseldorf",
        "13.107.42.14": "Cheney"
    }
    CreaTraza(google, posicion, 'green', "google: Bruselas, Bélgica", 2, m_g)
    CreaTraza(instagram, posicion, 'red',
              "instagram: Bruselas, Bélgica", 2, m_i)
    CreaTraza(lidenking, posicion, 'blue',
              "lidenking: Bruselas, Bélgica", 2, m_l)


if __name__ == '__main__':
    m_g = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    m_i = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    m_l = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    Amsterdam(m_g, m_i, m_l)
    Bruselas(m_g, m_i, m_l)
    m_g.save('mapa_google_Europa.html')
    m_i.save('mapa_instagram_Europa.html')
    m_l.save('mapa_lidenking_Europa.html')
