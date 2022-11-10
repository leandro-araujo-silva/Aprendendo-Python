valor = int(input('Digite um valor: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(valor, c, valor*c))
print('Essa é tabuada do {}'.format(valor))