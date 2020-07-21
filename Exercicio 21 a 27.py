# Exercicio 22
'''noms = input('Digite um nome: ')
tt1 = noms.split()
tt2 = ''.join(tt1)
print('Seu nome em maiusculo é {}'.format(noms.upper()))
print('Seu nome em minusculo é {}'.format(noms.lower()))
print('Seu nome ao tem {}'.format(len(tt2)))
print('Seu primeiro nome é {}'.format(len(tt1[0])))'''

# Exercicio 23
'''num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))'''

#Exercicio 24 Errado
cid = str(input('Nome de uma cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
if print == 'SANTO':
    print('Tem Santo aqui')
else:
    print('Não se salva ninguém')
#Exercicio 25
nome = str(input('Digite um nome: ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))
if print == 'silva':
    print('Tem silva nessa selva')
else:
    print('Não tem silva nem silva')
#Exercicio 26
'''palavra = input('Digite algo: ')
palavra1 = palavra.upper()
letra = palavra1.count('A')
procur = palavra1.find('A')
ult = palavra1.rfind('A')
print('A letra A aparece {} no texto'.format(letra))
print('A letra A aparece a primeira vez na posição {}'.format(procur))
print('A letra A aparece a ultima vez na posição {}'.format(ult))'''

#Exercicio 27
nome = input('Digite um nome: ')
n1 = nome.split()
print('Seu primeiro nome é:{}'.format(n1[0]))
print('Seu ultimo nome é {}'.format(n1[-1]))