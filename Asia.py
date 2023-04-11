import folium

def CreaTraza():
    o = [(posicion[youtube[ip]]['y'], posicion[youtube[ip]]['x'])
         for ip in youtube]
    d = [(posicion[youtube[ip]]['y'], posicion[youtube[ip]]['x'])
         for ip in list(youtube.keys())[1:]]
    c = [youtube[ip] for ip in youtube]
    i=0

    for ip in list(youtube.keys()):
        name = c[i]       
        o_lat, o_lon = o[i]
        folium.Marker(location=[o_lat, o_lon], popup=name+" ip:"+ip).add_to(m)
        if i<len(d):
            d_lat, d_lon = d[i]
            folium.Marker(location=[d_lat, d_lon], popup=name+" ip:"+ip).add_to(m)
            folium.PolyLine(locations=[(o_lat, o_lon), (d_lat, d_lon)],tooltip=f'', color='red',weight=2).add_to(m)
            i+=1

def Delhi():
    # Asia del Sur: New delhi, India
    posicion = {
        "Delhi": {'y': 28.6542, 'x': 77.2373},
        "Mumbai": {'y': 19.0748, 'x': 72.8856},
        "Greater Noida": {'y': 28.6145, 'x': 77.3063},
        "Cheney": {'y': 37.751, 'x': -97.822},
        "Bellevue": {'y': 47.6034, 'x': -122.3414},
        "Irving": {'y': 32.7797, 'x': -96.8022},
        "Greater Noida": {'y': 28.6145, 'x': 77.3063},
        "Cheney": {'y': 37.751, 'x': -97.822},
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

    m = folium.Map(location=[posicion['Bellevue']['y'],
                             posicion['Bellevue']['x']], zoom_start=7)



    
    m.save('mapa_asia.html')

def Tokio():
    # Asia del Este: Tokio, Japón
    google = {
        '31.204.145.130': {"ciudad": "Tokio", 'y': 35.6164, 'x': 139.7425},
        '101.203.88.173 ': {"ciudad": "kawasaki", 'y': 35.6897, 'x': 139.7425},
        '108.170.242.193': {"ciudad": "Cheney", 'y': 37.751, 'x': -97.822},
        '142.250.207.14': {"ciudad": "Bellevue", 'y': 47.6034, 'x': -122.3414}
    }
    docomo = {
        '31.204.145.131': {"ciudad": "Tokio", 'y': 35.6164, 'x': 139.7425},
        '210.171.224.211': {"ciudad": "kawasaki", 'y': 35.6897, 'x': 139.6895},
        '52.93.66.40': {"ciudad": "Ichikawa", 'y': 35.6893, 'x': 139.6899},
        '52.223.34.187': {"ciudad": "Cheney", 'y': 37.751, 'x': -97.822}
    }
    yahoo = {
        '31.204.145.131': {"ciudad": "Tokio", 'y': 35.6164, 'x': 139.7425},
        '101.203.88.39': {"ciudad": "kawasaki", 'y': 35.6897, 'x': 139.6895},
    }


if __name__ == '__main__':
    Delhi()
    #  m.save('mapa_asia.html')
