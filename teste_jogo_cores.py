import random

numero_secreto = random.randint(1, 5)
tentativas_restantes = 3

# Cores
VERDE = '\033[32m'
VERMELHO = '\033[31m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
RESET = '\033[0m'

# Começo do jogo
nome = str(input(f"\n{AZUL}Olá!!! Como é o seu nome? {RESET}"))
print(f"\n{AZUL}Olá {nome}, vamos jogar um jogo. Você deve adivinhar qual é o número entre 1 e 5.")
print(f"\nVocê tem 3 tentativas! Boa sorte!{RESET}")

while tentativas_restantes > 0:
    try:
        jogo = int(input(f"\n{AMARELO}Tente adivinhar o número: {RESET}"))

        # Verificação do intervalo
        if jogo < 1 or jogo > 5:
            print(f"{VERMELHO}⚠️ Por favor, digite um número entre 1 e 5.{RESET}")
            continue  # não gasta tentativa
    except ValueError:
        print(f"{VERMELHO}⚠️ Entrada inválida! Digite um número inteiro entre 1 e 5.{RESET}")
        continue  # não gasta tentativa

    if jogo == numero_secreto:
        print(f"{VERDE}🎉 Parabéns {nome}! Você acertou o número e ganhou o jogo!{RESET}")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"{VERMELHO}❌ Errou! Você ainda tem {tentativas_restantes} tentativa(s).{RESET}")
        else:
            print(f"{VERMELHO}💀 Que pena {nome}, suas tentativas acabaram! O número era {numero_secreto}.{RESET}")
