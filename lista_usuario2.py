from usuario2 import user

continuar = 1
lista_usuarios = []

while continuar != 0:
    sobrenome = input("Digite o seu sobrenome: ")    
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))        
    usuario2 = user(sobrenome, nome, idade)
    lista_usuarios.append(usuario2)

    #print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")
    print("Continuar cadastro? ")
    continuar = int(input("0-SAIR  1-CONTINUAR "))

else:
     for x in lista_usuarios:
        print(f"Nome: {x.nome} {x.sobrenome} / Idade: {x.idade}")   
