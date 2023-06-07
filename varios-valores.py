soma = 0
cont = 0
repete = -1

while repete != 999:
    repete = int(input('Digite um número [999 para parar]: '))
    
    if repete != 999:
        soma += repete
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))