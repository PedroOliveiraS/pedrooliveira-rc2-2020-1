import socket
import random

BUFSIZE = 65535


def server(interface):
    playersAddres = []
    playersLogins = []
    playersTries = []
    playersPoints = [1000, 1000, 1000]
    numP = 0
    port = 7100

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))

    while True:
        if numP == 3:
            for i in range(len(playersAddres)):
                print('Todos os jogadores foram conectados \n\n')
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

    ###play_guess.play()
    msg = '\n********************************\nBem vindo ao jogo da adivinhacao\n********************************'
    msg = bytes(msg.encode('ascii'))
    for i in range(len(playersAddres)):
        sock.sendto(msg, playersAddres[i-1])

    secret_number = random.randrange(1,101);
    print(secret_number)
    points = 1000;

    msg = 'O primeiro jogador definira a dificuldade do jogo'
    msg = bytes(msg.encode('ascii'))
    for i in range(len(playersAddres)):
        sock.sendto(msg, playersAddres[i-1])

    msg = 'Defina o nivel da dificuldade\n(1) Facil (2) Medio (3) Dificil'
    msg = bytes(msg.encode('ascii'))
    sock.sendto(msg, playersAddres[0])
    level, address = sock.recvfrom(BUFSIZE)
    level = int(level.decode('ascii'))

    if level == 1:
        playersTries = [20,20,20]
        msg = 'Dificuldade escolhida foi [facil]'
    elif level == 2:
        playersTries = [10,10,10]
        msg = 'Dificuldade escolhida foi [Medio]'
    else:
        playersTries = [5,5,5]
        msg = 'Dificuldade escolhida foi [Dificil]'

    msg = bytes(msg.encode('ascii'))
    for i in range(len(playersAddres)):
        sock.sendto(msg, playersAddres[i-1])

    order = [0, 1, 2]
    random.shuffle(order)
    random.shuffle(order)

    cont = -1
    cont1 = -1
    while playersTries[0] != 0 or playersTries[1] != 0 or playersTries[2] != 0:
        cont1 += 1
        cont += 1
        if cont1 == 3:
            cont1 = 0

        print('Rodada : ' + (str((cont+1))) + 'num = ' + str(cont1))
        msg = 'Rodada ' + str((cont+1)) + '\n'
        msg = bytes(msg.encode('ascii'))
        for i in range(len(playersAddres)):
            sock.sendto(msg, playersAddres[i-1])

        msg = '\nJogador ' + playersLogins[order[cont1]] + ' faca seu chute \n Voce tem mais ' + str(playersTries[order[cont1]]) +' tentativas'
        msg += '\nFaca sua escolha jogador [' + playersLogins[order[cont1]] + ']. Digite um numero entre 1 e 100'
        msg = bytes(msg.encode('ascii'))
        sock.sendto(msg, playersAddres[order[cont1]])
        playersTries[order[cont1]] = playersTries[order[cont1]] - 1

        while True:
            data, address = sock.recvfrom(BUFSIZE)
            if data:
                break

        guess = int(data);

        correct = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if guess < 1 or guess > 100:
            msg = 'Voce deve digitar um numero entre 1 e 100!'
            msg = bytes(msg.encode('ascii'))
            sock.sendto(msg, playersAddres[order[cont1]])
            playersPoints[order[cont1]] -= abs(secret_number - 100)
            continue

        if correct:
            msg = 'O player [' + playersLogins[order[cont1]] + '] acertou o numero.\n'
            msg = bytes(msg.encode('ascii'))
            for i in range(len(playersAddres)):
                sock.sendto(msg, playersAddres[i-1])
            playersPoints[order[cont1]] += abs(level*(cont-playersTries[order[cont1]]))
            break
        else:
            if bigger:
                msg = 'O player [' + playersLogins[order[cont1]] + '] chutou o numero ' + str(guess)+ '. Errou. O chute foi maior que o numero secreto.\n'
            elif smaller:
                msg = 'O player [' + playersLogins[order[cont1]] + '] chutou o numero ' + str(guess) + '. Errou. O chute foi menor que o numero secreto.\n'
            msg = bytes(msg.encode('ascii'))
            playersPoints[order[cont1]] -= abs(secret_number - guess);
            for i in range(len(playersAddres)):
                sock.sendto(msg, playersAddres[i-1])



    msg = 'Fim de jogo. Pontuacoes finais: \n' + playersLogins[0] + ' ficou com [' + str(playersPoints[0]) + ']\n'+\
          playersLogins[1] + ' ficou com [' + str(playersPoints[1]) + ']\n' + playersLogins[2] + ' ficou com [' + \
          str(playersPoints[2]) + ']'
    msg = bytes(msg.encode('ascii'))
    for i in range(len(playersAddres)):
        sock.sendto(msg, playersAddres[i - 1])


if __name__ == '__main__':
    server("")