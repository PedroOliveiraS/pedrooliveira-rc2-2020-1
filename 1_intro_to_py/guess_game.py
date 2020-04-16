print("\n********************************");
print("Bem vindo ao jogo da adivinhação");
print("********************************\n");

secret_number = 42;
tries = 3;
run = 1;

while tries:
    print("\nTentativa", run, "de", tries);
    guess_str = input("Qual seu chute: \n-> ");
    guess = int(guess_str);

    correct = guess == secret_number;
    bigger = guess > secret_number;
    smaller = guess < secret_number;

    if correct:
        print("Acertou");
    else:
        if bigger:
            print("Errou! O chute foi maior que o número secreto");
        elif smaller:
            print("Errou! O chute foi menor que o número secreto");
    run+=1;
    tries-=1;

print("Fim de jogo");