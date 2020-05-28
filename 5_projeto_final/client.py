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

        if data:
            newData = data.decode('ascii')
            if 'Fim de jogo' in newData:
                print(newData)
                break
            elif 'Defina o nivel' in newData:
                print(newData)
                msg = str(input())
                msg = bytes(msg.encode('ascii'))
                sock.send(msg)
            elif 'faca seu chute' in newData:
                print(newData)
                chute = str(input())
                chute = bytes(chute.encode('ascii'))
                sock.send(chute)
            else:
                print(newData)
    sock.close()
if __name__ == '__main__':
    client('192.168.1.9', 7100)