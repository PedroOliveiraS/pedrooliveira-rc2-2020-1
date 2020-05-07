import socket

MAX_BYTES = 65535


def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Saindo do modo promíscuo e aceitando respostas
    # apenas do servidor hostname
    sock.connect((hostname, port))
    print('Client socket name is {}'.format(sock.getsockname()))

    delay = 0.1  # atraso em segundos
    text = 'This is another message'
    data = text.encode('ascii')

    while True:
        # O cliente envia os dados e fica aguardando a resposta.
        # Um timeout é configurado para a espera.
        # Caso o timeout seja alcaçado, um novo envio é realizado.
        sock.send(data)
        print('Waiting up to {} seconds for a reply'.format(delay))
        sock.settimeout(delay)

        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout as exc:
            # se a resposta não for recebida dentro do intervalo
            # estabelecido, a exceção é acionada e o intervalo de
            # espera é dobrado
            delay *= 2

            # Se a espera for maior que 2 segundos o cliente
            # desiste da solicitação
            if delay > 2.0:
                raise RuntimeError('I think the server is down') from exc
        else:
            break   # Se a resposta é recebida, saímos do loop.

    print('The server says {!r}'.format(data.decode('ascii')))


if __name__ == '__main__':
    client('192.168.1.7', 1060)