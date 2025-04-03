from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:    
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    sobrenome = input("Digite o seu sobrenome: ")    
    usuario = Usuario(nome, idade, sobrenome)
    lista_usuarios.append(usuario)

    #print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")
    print("Continuar cadastro? ")
    continuar = int(input("0-SAIR  1-CONTINUAR "))

else:
     for x in lista_usuarios:
        print(f"Nome: {x.nome} {x.sobrenome} / Idade: {x.idade}")  
