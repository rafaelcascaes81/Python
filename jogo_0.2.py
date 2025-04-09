import random

numero_secreto = random.randint(1, 5)
tentativas_restantes = 3

nome = str(input("Olá!!! Como é o seu nome? "))
print(f"Olá {nome}, vamos jogar um jogo. Você deve adivinhar qual é o número entre 1 e 5.")
print("Você tem 3 tentativas!")

while tentativas_restantes > 0:
    jogo = int(input("Tente adivinhar o número: "))

    if jogo == numero_secreto:
        print(f"Parabéns {nome}! Você acertou o número e ganhou o jogo!")
        break  # encerra o loop se acertar
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Errou! Você ainda tem {tentativas_restantes} tentativa(s). Tente novamente.")
        else:
            print(f"Que pena {nome}, suas tentativas acabaram! O número era {numero_secreto}.")
