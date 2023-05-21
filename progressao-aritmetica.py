a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a10 = a1 + (10 - 1)*r

for c in range(a1,a10 + 1, r):
    print('{} '.format(c), end=' -> ')
print('Acabou.')