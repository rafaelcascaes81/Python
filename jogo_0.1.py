import random

numero_secreto = random.randint(1, 5)
jogo = 0

nome = str(input("Olá!!! Como é o seu nome? "))
print(f"Olá {nome}, vamos jogar um jogo. Você deve adivinhar qual é o número entre 1 e 5.")

while jogo != numero_secreto:
    jogo = int(input("Tente adivinhar o número de 1 a 5: "))
    if jogo == numero_secreto:
        print(f"Parabéns {nome}! Você acertou o número e ganhou o jogo!")
    else:
        print("Errou!!! Tente novamente.")
