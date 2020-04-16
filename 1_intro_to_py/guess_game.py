print("\n********************************");
print("Bem vindo ao jogo da adivinhação");
print("********************************\n");

secret_number = 42;
guess = input("Digite o seu número: \n-> ");
print("Você digitou: ",guess)

if (secret_number == int(guess)):
    print("Acertou");
else:
    print("Errou");

print("Fim de jogo");