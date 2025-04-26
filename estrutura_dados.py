lista = [10,99,37,40]
print(f'A lista é mutavel {lista}')

tupla = (10,2,30,40)
print(f'A tupla é imutavel {tupla}')

##Conjuntos - união - interseção - diferença
conjunto = {5, 1, 2, 3, 3, 4, 4}
print("Conjunto sempre vai ordenar e excluir repetidos")
print(f'Conjunto homogeneo {conjunto}')

conjunto1 = {1,2,3,4,5,6}
conjunto2 = {4,5,6,7,8,9,10}

##União
print(conjunto1 | conjunto2) ##uniao com |
print(conjunto1.union(conjunto2)) ##uniao com função union

##interseção
print(conjunto1 & conjunto2) ##interseção com &
print(conjunto1.intersection(conjunto2)) ##interseção com função intersection

##diferença
print(conjunto1 - conjunto2) ##diferença com -
print(conjunto1.difference(conjunto2)) ##diferença com funçao difference

##Dicionario
dic1 = {1: 'Rafael', 2: 'Tais', 3: 'Pantanal', 4: 'Floripa'}
print(dic1)
print(dic1[4])
print(f'O {dic1[1]} é casado com a {dic1[2]} eles moram no {dic1[3]} ')
