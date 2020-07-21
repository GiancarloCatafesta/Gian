#Exericicio 16
'''import math
n = float(input("Digite um numero: "))
inter = math.floor(n)
print('Seu numero é {}, sua versão inteira é {}'.format(n,inter))'''

#Exercício 17
'''import math
a = float(input('Digite uma medida: '))
b = float(input('Digite outra medida: '))
hipo = math.hypot(a,b)
print('O valor da soma dos catetos é de {}, sendo o valor da hipotenusa'.format(hipo))'''

#Exercicio 18
'''import math
n = int(input('digite um angulo: '))
nc = math.cos(n)
ns = math.sin(n)
nt = math.tan(n)
print('Seu angulo é {}. Seu cosseno é {},seu seno é {} e sua tangente é {}'.format(n,nc,ns,nt))'''

#Exercicio 19
'''import random
alun = ['Pipinha', 'João', 'Maria', 'Zé']
esco = random.choice(alun)
print('O aluno escolhido foi {}'.format(esco))'''

#Exercicio 20
'''import random
alunos = ['goberto','jose','pipinha','maria']
orde = random.shuffle(alunos)
print('A ordem escolhida foi {}'.format(alunos))'''

#Exercicio 21
import playsound
parar = str(input("Diga para para parar se quiser.")).upper()
playsound.playsound('Bring Me The Horizon - Doomed (Live at the Royal Albert Hall).mp3')
if parar == "PAUSE":
    stop.sound(playsound.playsound)
else:
    playsound.playsound




