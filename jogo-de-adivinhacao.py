import random

def numero_aleatorio_intervalo(a, b):
    return random.randint(a, b)

# Exemplo de uso da função
num = numero_aleatorio_intervalo(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

escolhido = -1
tentativas = 1

while num != escolhido:
    escolhido = int(input('Qual é o seu palpite? '))
    if escolhido > num:
        print('Menos... Tente mais uma vez.')
    elif escolhido < num:
        print('Mais... Tente mais uma vez.')
    else:
        print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
    tentativas += 1

