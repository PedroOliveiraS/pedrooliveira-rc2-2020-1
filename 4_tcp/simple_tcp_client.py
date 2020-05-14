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


def client(host, port):
    # Criando socket TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Solicitando conexão com o servidor na porta especifica
    sock.connect((host, port))

    # Printando informações da conexão
    print('Client has been assigned socket name', sock.getsockname())

    # Enviando os dados para o servidor
    sock.sendall(b'Hi there, server')

    # Aguardando a resposta do servidor
    reply = recvall(sock, 16)

    # Apresentando a resposta do servidor
    print('The server said', repr(reply))

    # Fechando o socket, encerrando a sessão
    sock.close()


if __name__ == '__main__':
    client("127.0.0.1", 1060)