#Exercicio 28
import random
from playsound import playsound
seunum = 'Computador. Pense em um numero''\n Ookk'
print(seunum)
meunum = int(input('Seu numero é : '))
num = random.randint(0,1)
print('Meu numero é {}'.format(num))
if meunum == num:
    print('Se é um bichão memo')
    playsound('Maluco e brabo.mp3.mpeg')
else:
    print('Errrrooooouuu')

#Exercicio 29
import emoji
print(emoji.emojize('Se correr é corno:cow:'))
veloc = float(input('Qual a velocidade do carro: '))
print(f'Seu carro está a {veloc} km/h')
if veloc > 80.00:
    print('Seu filha da égua. Vai tirar a mãe da zona?')
    mult = (veloc - 80)*7.00
    print(f'Você foi multado em R${mult}, por estar acima da velocidade de 80km/h')
else:
    print("Andando delicia")

#Exercicio 30
n = int(input('Digite um numero:'))
if n % 2 == 0:
    print('{} é um numero par'.format(n))
else:
    print('{} é impar'.format(n))

#Exercicio 31
viagem = int(input('Qual a distancia da sua viagem:'))
print(viagem)
if viagem > 200:
    valor1 = viagem * 0.45
    print('Sua passagem irá custar R${}'.format(valor1))
else:
    valor2 = viagem * 0.50
    print('Sua passagem irá custar R${}'.format(valor2))

#Exercicio 32
ano = int(input('Digite um ano: '))
if (ano % 4 == 0 and ano % 100!=0) or (ano % 400==0):
    print(f"{ano} é ano bissexto")
else:
    print('Não é ano bisexo')

#Exercicio 33
primeiro = int(input('Digite um numero: '))
segundo = int(input('Digite outro numero: '))
terceiro = int(input('Digite mais um numero: '))
maior = primeiro
if segundo>maior:
    maior = segundo
if terceiro>maior:
    maior = terceiro
print('Maior: ',maior)
menor = primeiro
if segundo<menor:
    menor = segundo
if terceiro<menor:
    menor = terceiro
print('Menor: ',menor)
print('O maior é {} e o menor é {}'.format(maior,menor))

#Exercicio 34
salar = float(input('Qual o salário do funcionário:'))
if salar > 1250.00:
    aum = salar * 0.10
    total = salar + aum
    print(f"Vai ter um aumento de R${aum}, dando um total de R${total}")
else:
    aume = salar * 0.15
    total = salar + aume
    print(f'Vai ter um aumnento de R${aume}, dando um aumento de R${total}')

#Exercicio 35
#Cada reta tem que ser menor que a soma do comprimento das outras retas
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Você tem um triangulo')
else:
    print('Não é possível formar um triangulo')
