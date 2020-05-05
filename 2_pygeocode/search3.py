import http.client
import json
from urllib.parse import quote_plus

base = '/search'


def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Search3.py'
    headers = {b'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(f'Endereço Buscado: {address}')

    for i in range(len(reply)):
        print(f"Resultado {i}:")
        print("     CEP: {}".format(reply[i]['display_name'].split(",")[-2]))
        print("     (Latitude, Longitude): ({})".format(reply[i]['lat'], reply[i]['lon']))


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')