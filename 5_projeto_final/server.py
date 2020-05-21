import socket

BUFSIZE = 65535


def server(interface):
    playersAddres = []
    playersLogins = []
    numP = 0
    port = 7100

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))

    while True:
        if numP == 3:
            for i in range(len(playersAddres)):
                send = '0'
                print('Enviando: ', send)
                newMessage = bytes(send.encode('ascii'))
                sock.sendto(newMessage, playersAddres[i - 1])
            break;
        else:
            print('\n\n\n')
            print('Aguardando conexões...')
            data, address = sock.recvfrom(BUFSIZE)

            if(address):
                numP = numP + 1
                playersAddres.append(address)
                print(str(data.decode('ascii')) + ' conectado com sucesso.')
                playersLogins.append(str(data.decode('ascii')))

            print('Jogadores na sala:')
            for i in range(len(playersAddres)):
                for j in range(len(playersAddres)):
                    send = playersLogins[j - 1] + ' esta conectado.'
                    print('Enviando a: ',playersAddres[i-1], 'a mensagem: ', send)
                    newMessage = bytes(send.encode('ascii'))
                    sock.sendto(newMessage, playersAddres[i - 1])

            if numP != 3:
                for i in range(len(playersAddres)):
                    send = 'Aguardando ' + str((3 - numP)) + ' jogadores.'
                    print('Enviando: ', send)
                    newMessage = bytes(send.encode('ascii'))
                    sock.sendto(newMessage, playersAddres[i - 1])


if __name__ == '__main__':
    server("")