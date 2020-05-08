import random
import socket

MAX_BYTES = 65535


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listening at', sock.getsockname())

    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('O cliente em {} nos disse: {!r}. Vamos responder ele com a mesma mensagem em caixa alta.'.format(address, text))
    message = text.upper()
    sock.sendto(message.encode('ascii'), address)


if __name__ == '__main__':
    # Aqui, "" significa que o servidor está habilitado a receber
    # requisições de qualquer umas das interfaces locais
    server("", 1060)