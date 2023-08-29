'''
# ARMAZENAR MAIS DE UMA INFORMAÇÃO EM VARIAVEIS 
#MANTER A SEQUENCIA DOS DADOS EM UMA VARIAVEL


Cidade1 = 'rio de janeiro'
Cidade2 = 'são paulo'
Cidade3 = 'salvador'

cidades = [ ' rio de janeiro', 'são paulo', 'salvador']
#                  0                 1           2

#cidades.append('santa catarina)
#cidades.remove('salvador)
#cidades.insert('2,'manaus)
#cidades.pop(0)
cidades.sort()


print(cidades)
'''

numeros = [2,3,4,5]
letras = ['a','b','c','d']

#final = numeros + letras
numeros.extend(letras)
print(numeros)


#itens = ['item1','item2','item3','item4']
 
itens = [['item1','item2'],['item3','item4']]
 #            0       1         0        1
print(itens[1])

