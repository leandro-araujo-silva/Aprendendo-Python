from datetime import date
anoAtual = date.today().year

nascimento = int(input('Digite seu ano de nascimento:'))
anos = anoAtual - nascimento
cont = 0

print('Você nasceu em {} e possui {} anos. '.format(nascimento, anos))

if anos > 18:
    cont = anos - 18
    alistamento = anoAtual - cont
    print('Você já deveria ter se alistado há {} anos.'.format(cont))
    print('Seu alistamento foi em {}.'.format(alistamento))
elif anos == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
else:
    cont = 18 - anos
    alistamento = anoAtual + cont
    print('Ainda faltam {} anos para o alistamento.'.format(cont))
    print('Seu alistamento será em {}.'.format(alistamento))