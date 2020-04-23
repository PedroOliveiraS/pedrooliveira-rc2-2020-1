import random

def play():
    # Chama a mensagem de abertura
    print_opening()

    # Carrega a palavra secreta
    secret_word = load_secret_word()

    print(secret_word)

def print_opening():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def load_secret_word():
    # Esta função sorteia uma palavra secreta a partir de uma
    # lista de palavras armazenadas em um arquivo externo

    # Abre o arquivo em modo leitura (r)
    file = open("words.txt", "r")

    # Lista para armazenar as palavras
    words = []

    for line in file:           # Para cada linha do arquivo
        line = line.strip()     # remove o \n no final da linha
        words.append(line)      # Insere a palavra na lista

    #fecha o arquivo
    file.close()

    # Sorteia um número para escolher a palavra secreta
    number = random.randrange(0, len(words))

    # Seleciona a palavra secreta, colocando todas as letras
    # em maiúsculo e a retorna
    secret_word = words[number].upper()
    return secret_word

if __name__ == "__main__":
    play();