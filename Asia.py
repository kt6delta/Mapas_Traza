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


def Delhi(m_g, m_i, m_l):
    # Asia del Sur: New delhi, India
    posicion = {
        "Delhi": {'y': 28.6542, 'x': 77.2373},
        "Mumbai": {'y': 19.0748, 'x': 72.8856},
        "Greater Noida": {'y': 28.6145, 'x': 77.3063},
        "Cheney": {'y': 37.751, 'x': -97.822},
        "Bellevue": {'y': 47.6034, 'x': -122.3414},
        "Irving": {'y': 32.7797, 'x': -96.8022},
        "Bangalore": {'y': 12.9634, 'x': 77.5855},
        "Calcuta": {'y': 22.518, 'x': 88.3832},
        "Chaurai": {'y': 21.9974, 'x': 79.0011}
    }

    google = {
        '164.52.192.1':  'Delhi',
        '180.179.210.65': 'Mumbai',
        '14.141.116.105': 'Delhi',
        '14.140.113.238': 'Greater Noida',
        '74.125.244.193': 'Cheney',
        '142.250.206.142': 'Bellevue'
    }

    youtube = {
        '164.52.192.1':  "Delhi",
        '180.179.210.65': "Mumbai",
        '14.141.116.105': "Delhi",
        '14.140.113.238': "Greater Noida",
        '108.170.251.113': "Cheney",
        '142.251.49.121': "Irving",
        '142.250.194.78': "Bellevue"
    }

    facebook = {
    '164.52.192.1':  'Delhi',
    '180.179.210.65': 'Mumbai',
    '125.19.53.93': 'Bangalore',
    '116.119.109.252': 'Chaurai',
    '157.240.82.168': 'Cheney',
    '157.240.1.35': 'Calcuta'
    }

    CreaTraza(google, posicion, 'green', "google: New delhi, India", 2, m_g)
    CreaTraza(youtube, posicion, 'red', "youtube, New delhi, India", 2, m_i)
    CreaTraza(facebook, posicion, 'blue', "facebook,New delhi, India", 2, m_l)


def Tokio(m_g, m_i, m_l):
    posicion = {
        "Tokio": {'y': 35.6164, 'x': 139.7425},
        "kawasaki": {'y': 35.6897, 'x': 139.7425},
        "Cheney": {'y': 37.751, 'x': -97.822},
        "Bellevue": {'y': 47.6034, 'x': -122.3414},
        "Ichikawa": {'y': 35.6893, 'x': 139.6899},
    }

    # Asia del Este: Tokio, Japón
    google = {
        '31.204.145.130': "Tokio",
        '101.203.88.173 ': "kawasaki",
        '108.170.242.193': "Cheney",
        '142.250.207.14': "Bellevue"
    }
    docomo = {
        '31.204.145.131': "Tokio",
        '210.171.224.211': "kawasaki",
        '52.93.66.40': "Ichikawa",
        '52.223.34.187': "Cheney",
    }
    yahoo = {
        '31.204.145.131': "Tokio",
        '101.203.88.39': "kawasaki",
    }
    CreaTraza(google, posicion, 'grey',"google: Tokio, Japón",2,m_g)
    CreaTraza(docomo, posicion, 'black',"docomo: Tokio, Japón",2,m_i)
    CreaTraza(yahoo, posicion, 'purple',"yahoo: Tokio, Japón",2,m_l)

if __name__ == '__main__':
    m_g = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    m_i = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    m_l = folium.Map(location=["20.17794001195229",
                     "-2.9395183635160786"], zoom_start=2)
    
    Delhi(m_g, m_i, m_l)
    Tokio(m_g, m_i, m_l)
    m_g.save('mapa_google_Asia.html')
    m_i.save('mapa_youtube_Asia.html')
    m_l.save('mapa_facebook_Asia.html')
