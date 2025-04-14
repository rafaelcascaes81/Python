listaidade = [27, 44, 88, 12, 98, 2, 3, 37]
maior_idade = 0

for idade in listaidade:
    if idade > maior_idade:
        maior_idade = idade

print(f"A maior idade é {maior_idade}")

listaidade.append(102) ##append adiciona elemento na lista

for idade in listaidade:
    if idade > maior_idade:
        maior_idade = idade

print(f"A maior idade agora é {maior_idade}")        
print(listaidade)

lista1 = [10, 20, 30]
lista2 = [40, 50, 60]
lista3 = [100, 200, 300]
print(lista1 + lista2)
print(len(lista3)) ##len retorna a quantidade dos elementos da lista
print(sum(lista1)) ##sum retorna a soma dos elementos da lista
print(max(lista3)) ##max retorna o maior elemento da lista
print(sorted(listaidade)) ##ordena os elementos da lista