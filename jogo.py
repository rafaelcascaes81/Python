jogo = 1
nome = str(input("Ola!!! Como é o seu nome? "))
print(f"Ola {nome} vamos jogar um jogo, voce deve adivinhar qual é o numero")
while jogo != 3:
    jogo = int(input("tente advinhar o numero de 1 a 5: "))
    if jogo == 3:
        print(f"Parabens {nome} voce acertou o numero e ganhou o jogo")
    else:
        print("errou!!! tente novamente")
