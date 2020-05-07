import random
import socket

MAX_BYTES = 65535


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listening at', sock.getsockname())

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        # Sorteando um número para decidir se
        # o pacote será descartado ou não.
        if random.random() < 1:
            print('Pretending to drop packet from {}'.format(address))
            continue
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        message = 'Your data was {} bytes long'.format(len(data))
        sock.sendto(message.encode('ascii'), address)


if __name__ == '__main__':
    # Aqui, "" significa que o servidor está habilitado a receber
    # requisições de qualquer umas das interfaces locais
    server("", 1060)