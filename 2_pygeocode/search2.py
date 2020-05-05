import requests

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print(f'Endereço Buscado: {address}')

    for i in range(len(reply)):
        print(f"Resultado {i}:")
        print("     CEP: {}".format(reply[i]['display_name'].split(",")[-2]))
        print("     (Latitude, Longitude): ({})".format(reply[i]['lat'], reply[i]['lon']))


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')