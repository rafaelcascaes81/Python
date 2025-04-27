##Tradicional
def multi2(num):
    return num * 2

print(multi2(4))

##Lambda
lam = lambda num: num * 2
print(lam(4))


nome = 'Tais'
if len(nome) > 5:
    tamanho = 'GRANDE'
else:
    tamanho = 'pequeno'
print(f'O nome {nome} é {tamanho}')


nome2 = 'Rafael'
tamanho2 = 'Grande' if len(nome2) > 5 else 'Pequeno'
print(f'O {nome2} é {tamanho2}')