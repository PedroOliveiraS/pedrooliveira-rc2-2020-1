import socket
from datetime import datetime

# Número máximo de bytes que podem ser enviados
# de uma vez só com o UDP
MAX_BYTES = 65535


def client(port):
    # Criando um socket
    # AF_INET: utilizando a pilha de protocolos da Internet
    # SOCK_DGRAM: selecionando o protocolo UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Preparamos os dados da solicitação
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')

    # Enviamos os dados para o endereço do servidor
    # na porta adequada (default = 1060)
    sock.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))

    # Ficamos aguardando a resposta do servidor
    data, address = sock.recvfrom(MAX_BYTES)

    # Apresentamos a resposta decodificada na saída padrão
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))


if __name__ == '__main__':
    # Execução da função com a porta do nosso servidor
    client(1060)