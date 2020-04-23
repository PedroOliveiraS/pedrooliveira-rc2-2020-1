import hangman_game
import guess_game

def choose_game():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    game = int(input("(1) Forca (2) Adivinhação \n"))

    if game == 1:
        print("Jogando Forca")
        hangman_game.play()
    else:
        print("Jogando Adivinhação")
        guess_game.play()

if __name__ == "__main__":
    choose_game()