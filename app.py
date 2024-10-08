#### JOGO DE ADVINHAÇÃO DE NÚMEROS (TERMINAL)

from random import randint

# Sorteia o número
numero_sorteado = randint(1,101)

# Inicializando as variáveis
numero_digitado = 0
numero_tentativas = 0

while numero_sorteado != numero_digitado:

    # Solicita o usuário digitar o número
    numero_digitado = int(input("Digite o seu palpite: "))

    if numero_sorteado > numero_digitado:
        print(f"Você errou! O número sorteado é maior do que o digitado! Tente novamente!")

    elif numero_sorteado < numero_digitado:
        print(f"Você errou! O número sorteado é menor do que o digitado! Tente novamente!")

    else:
        print(f"Parabéns, você acertou! O número sorteado foi {numero_sorteado}, você precisou de {numero_tentativas} tentativas para acertar!")

    numero_tentativas += 1







