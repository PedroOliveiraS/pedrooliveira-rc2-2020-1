#!/usr/bin/env python3
import socket
import ssl
from urllib.parse import quote_plus

request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: Search4.py\r\n\
Connection: close\r\n\
\r\n\
"""


def geocode(address):
    unencrypted_sock = socket.socket()
    unencrypted_sock.connect(('nominatim.openstreetmap.org', 443))
    sock = ssl.wrap_socket(unencrypted_sock)
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    newraw = raw_reply.decode('utf-8')
    print(newraw)
    print("MEU DEUS DO CEU")

    print(type(newraw))
    altered = newraw.split('\n')
    tam = len(altered)
    dec = altered[tam-4]
    print(dec)
    #print(dec.find('lon'))
    #print(dec[235:300])
    #novo = dec[234:300]
    #print(novo)
    #print(dec['place_id'])

   # for i in range(len(raw_reply)):
   #     print(f"Resultado {i}:")
   #     print("     CEP: {}".format(raw_reply[i]['display_name'].split(",")[-2]))
   #     print("     (Latitude, Longitude): ({})".format(raw_reply[i]['lat'], raw_reply[i]['lon']))


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')