import socket

MAX_BYTES = 65535


def client(hostname, port, text):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Saindo do modo promíscuo e aceitando respostas
    # apenas do servidor hostname
    sock.connect((hostname, port))
    print('Client socket name is {}'.format(sock.getsockname()))

    data = text.encode('ascii')

    sock.send(data)
    data = sock.recv(MAX_BYTES)

    print('The server says {!r}'.format(data.decode('ascii')))


if __name__ == '__main__':
    text = input('Qual o texto você deseja enviar ao sevidor?')
    client('192.168.1.7', 1060, text)