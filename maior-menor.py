v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
v3 = float(input('Terceiro valor: '))
maior = v1
menor = v1
if v2 > v1 and v2 > v3:
  maior = v2
if v3 > v1 and v3 > v2:
  maior = v3
if v2 < v1 and v2 < v3:
  menor = v2
if v3 < v1 and v3 < v2:
  menor = v3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

