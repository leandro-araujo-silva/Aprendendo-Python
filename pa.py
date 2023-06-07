repete = -1
cont = 0

pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

for c in range(10):
    print(pt, end = ' -> ')
    pt += r
    cont += 1

print('PAUSA')

while repete != 0:
    repete = int(input('Quantos termos você quer mostrar a mais? '))
    cont += repete
    if repete == 0:
        print('Progressão finalizada com {} termos mostrados.'.format(cont))
    else: 
        for t in range(repete):
            print(pt, end = ' -> ')
            pt += r
        print('PAUSA')
