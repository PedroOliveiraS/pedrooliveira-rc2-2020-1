import socket

# Número máximo de bytes que podem ser enviados
# de uma vez só com o UDP
MAX_BYTES = 65535


def server(port):
    # Criando o socket
    # AF_INET: utilizando a pilha de protocolos da Internet
    # SOCK_DGRAM: selecionando o protocolo UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Ligando o socket ao endereço de localhost
    # e à porta indicada pelo usuário (default = 1060)
    sock.bind(('127.0.0.1', port))

    # getsockname retorna o nome do socket
    print('Listening at {}'.format(sock.getsockname()))

    # Loop aguardando as solicitações dos clientes
    while True:
        # A função recvfrom fica aguardando a chegada
        # da socilitação do cliente
        # Além dos dados enviados pelo cliente, também
        # conseguimos acessar o endereço IP do cliente
        data, address = sock.recvfrom(MAX_BYTES)

        # Decodificamos os dados para ascii e apresentamos
        # na sáida padrão
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))

        # Enviamos uma resposta à solicitação do cliente
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)


if __name__ == '__main__':
    # Execução da função com a porta do nosso servidor
    server(1060)