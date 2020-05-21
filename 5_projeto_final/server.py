import socket

BUFSIZE = 65535


def server(interface):
    players = []
    numP = 0
    ports = [62616, 53340, 57243]
    socks = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM), socket.socket(socket.AF_INET, socket.SOCK_DGRAM),
             socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]

    socks[0] = socks[0].bind((interface, ports[0]))
    socks[1] = socks[1].bind((interface, ports[1]))
    socks[2] = socks[2].bind((interface, ports[2]))

    print('Esperando por jogadores em: {}'.format(socks[0].getsockname()))

    while numP != 0:
        data, address = sock.recvfrom(BUFSIZE)
        text = data.decode('ascii')
        print('The client at {} says: {!r}'.format(address, text))


if __name__ == '__main__':
    server("")