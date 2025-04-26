##Criação abertura e fechamento de arquivos
# r modo somente leitura
# w modo de escrita, cria ou substitui o atual
# x modo de escrita, se o arquivo já existe retorna erro
# a modo de escrita cria um arquivo caso não exista, ou adiciona info ao final
# t abre o arquivo em modo texto
# b abre em modo binario

arquivo = open('escrita.txt' , 'r')
ler = arquivo.read()
arquivo.close()
print(ler)

arquivo = open('escrita.txt' , 'a')
arquivo.write('nova escrita no arquivo\n')
arquivo.close()