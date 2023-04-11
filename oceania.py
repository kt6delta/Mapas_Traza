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


def Australia(m_g, m_i, m_l):
    # Oceanía del Norte: Sídney, Australia
    posicion = {
        "Sídney": {'y': -33.8715, 'x': 151.2006},
        "": {'y': -33.494, 'x': 143.2104},
        "Cheney": {'y': 37.751, 'x': -97.822},
        "Fort Worth": {'y': 32.7254, 'x': -97.3208},
        "Springville": {'y': 33.7386, 'x': -86.4394}
    }
    google = {
        '221.121.154.216': "Sídney",
        '118.127.7.98': "",
        '108.170.247.81': "Cheney",
        '142.250.71.68': "Fort Worth"
    }
    instagram = {
        "221.121.154.216": "Sídney",
        "118.127.7.98":	"",
        "129.134.78.184":  "Cheney",
        "173.252.67.119": "Springville",
        "157.240.8.174": "Sídney"
    }
    lidenking = {
        "221.121.154.216": "Sídney",
        "104.44.236.58":  "Cheney",
        "13.104.183.81": "Sídney",
        "13.107.42.14 ":  "Cheney"
    }
    CreaTraza(google, posicion, 'green', "google: Sídney, Australia", 2, m_g)
    CreaTraza(instagram, posicion, 'red', "instagram, Sídney, Australia", 2, m_i)
    CreaTraza(lidenking, posicion, 'blue', "lidenking, Sídney, Australia", 2, m_l)


def Auckland(m_g, m_i, m_l):
    # Oceanía del Sur: Auckland, Nueva Zelanda
    posicion = {
        "Auckland": {'y': -36.8867, 'x': 174.769},
        "Christchurch": {'y': -43.5379, 'x': 172.6151},
        "Melbourne": {'y': -37.8159, 'x': 144.9669},
        "Cheney": {'y': 37.751, 'x': -97.822},
        "Springville": {'y': 33.7386, 'x': -86.4394},
        "Auckland2":{"y":- 36.8506, "x":174.7679},
        "Christchurch" :{"y": - 43.5379, "x" :172.6151},
        "": {"y":- 42.0009, "x":173.998}
    }
    google = {
        '49.50.246.153': "Auckland",
        '114.23.4.240': "Christchurch",
        '218.100.52.3': "Melbourne",
        '108.170.247.49': "Cheney"
    }
    instagram = {
        "49.50.246.153": "Auckland" ,
        "114.23.4.240": "Christchurch", 
        "129.134.47.77": "Cheney" ,
        "173.252.67.55": "Springville",
        "31.13.78.174":  "Auckland2"
    }
    lidenking = {
        "49.50.246.153":"Auckland" ,
        "114.23.4.240":"Christchurch" ,
        "192.203.154.163":"",
        "13.107.42.14": "Cheney"
    }
    CreaTraza(google, posicion, 'green', "google:  Nueva Zelanda", 2, m_g)
    CreaTraza(instagram, posicion, 'red', "instagram, Nueva Zelanda", 2, m_i)
    CreaTraza(lidenking, posicion, 'blue', "lidenking, Nueva Zelanda", 2, m_l)


if __name__ == '__main__':
    m_g = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    m_i = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    m_l = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    Australia(m_g, m_i, m_l)
    Auckland(m_g, m_i, m_l)
    m_g.save('mapa_google_Oceania.html')
    m_i.save('mapa_instagram_Oceania.html')
    m_l.save('mapa_lidenking_Oceania.html')
