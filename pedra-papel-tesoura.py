from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA 
''')

jogada = int(input('Qual é a sua jogada? '))

print('''-=-=-=-=-=-=-=-=-=-==-=-=-=
Máquina jogou {}
Jogador jogou {}
-=-=-=-=-=-=-=-=-=-=-=-=-='''.format(itens[computador], itens[jogada]))

if computador == 0 and jogada == 0 or computador == 1 and jogada == 1 or computador == 2 and jogada == 2:
    print('Empate!')
elif computador == 0 and jogada == 2 or computador == 1 and jogada == 0 or computador == 2 and jogada == 1:
    print('Máquina venceu jogador!')
else:
    print('Jogador venceu Máquina!')