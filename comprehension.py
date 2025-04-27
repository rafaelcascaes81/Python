##tradicional
lista = []
for lis in range(1,11):
    lista.append(lis)

print(f'Lista Normal: {lista}')


##Comprehension
lista2 = [lis for lis in range(1,11)]
print(f'Lista Comprehension: {lista2}')



##tradicional
dicionario = {}
for item in range(1, 11):
    dicionario[item] = item

print(f'Dicionario Normal: {dicionario}')


##Comprehension
dicionario2 = {item: item for item in range(1, 11)}
print(f'Dicionario Comprehension: {dicionario2}')