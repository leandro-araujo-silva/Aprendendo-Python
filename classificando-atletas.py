from datetime import date

anoAtual = date.today().year

nascimento = int(input('Ano de nascimento: '))

idade = anoAtual - nascimento

print('O atleta tem {} anos.'.format(idade))

if idade < 10:
    print('Classificação: JUNIOR')
elif idade < 15:
    print('Classificação: INFANTIL')
elif idade < 20:
    print('Classificação: JUNIOR')
elif idade < 26:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')