n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print('Sua média: {}'.format(media))

if media >= 7:
    print('Você está aprovado!')
elif media > 5 and media <= 6.9:
    print('Você está em recuperação!')
else: 
    print('Você está reprovado!')