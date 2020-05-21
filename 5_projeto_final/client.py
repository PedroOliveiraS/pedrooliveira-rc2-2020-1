import socket

BUFSIZE = 65535


def client(network, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((network,port))
    send = input('Login: ')
    sock.send(bytes(send.encode('ascii')))
    print('Tentando entrar na sala do jogo...')

    while True:
        data, adress = sock.recvfrom(BUFSIZE)

        if data == '0':
            break
        else:
            newData = data.decode('ascii')
            if newData != '0':
                print(str(data.decode('ascii')) + '\n')

    sock.close()
if __name__ == '__main__':
    client('192.168.137.1', 7100)