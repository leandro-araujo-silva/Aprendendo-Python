import random

x = random.randint(1, 5)
ne = int(input('Escolha um número de 0 a 5: '))

print('Valor sorteado: {}'.format(x))
if ne == x:
  print('Você acertou!')
else: 
  print('Você errou!')