soma = 0
maior = 0
menor = 9999999
repete = 's'
cont = 0

n = int(input('Digite um número: '))
maior = n
menor = n
soma += n
cont += 1

repete = str(input('Quer continuar? [S/N] ').lower().strip()[0])
while repete == 's':
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    repete = str(input('Quer continuar? [S/N] ').lower().strip()[0])

media = soma / cont

print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

