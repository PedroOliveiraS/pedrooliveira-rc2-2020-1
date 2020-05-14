import socket




def recvall(sock, length):
    data = b''

    # o laço é verdade enquanto não recebermos
    # todos os bytes esperados.
    # No caso deste programa simples são 16 bytes
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data


def server(interface, port):
    # Criando socket TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configurando as opções do socket
    # SOL_SOCKET indica o nível que a opção será aplicada.
    # Neste caso a opção é aplicada no próprio socket
    # SO_REUSEADDR possibilita o reúso das configurações de
    # endereço do socket, mesmo com a utilização da
    # função bind()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Configura o servidor para receber pacotes
    # apenas nas interfaces especificadas.
    # Se configurado como "" aceita pacotes de qualquer
    # interface do dispositivo
    sock.bind((interface, port))

    # Habilita o socket para aguardar solicitações
    # A função listen() na prática transforma o socket em
    # um socket passivo (ou listening socket)
    # O argumento 1 indica o tamanho da fila de solicitações
    sock.listen(1)
    print('Listening at', sock.getsockname())

    while True:
        print('Waiting to accept a new connection')
        # Aceita novas conexões
        # A cada nova conexão, um socket ativo (ou connected socket)
        # é criado e retornado na varíável sc
        sc, sockname = sock.accept()
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())

        # Aguardando o cliente enviar os dados
        message = recvall(sc, 16)
        print('  Incoming sixteen-octet message:', repr(message))

        # Envia resposta ao servidor
        sc.sendall(b'Farewell, client')

        # Encerra a sessão fechando o socket
        sc.close()
        print('  Reply sent, socket closed')


if __name__ == '__main__':
    server("127.0.0.1", 1060)