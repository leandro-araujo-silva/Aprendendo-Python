import datetime

def obter_ano_atual():
    ano_atual = datetime.datetime.now().year
    return ano_atual

ano_atual = obter_ano_atual()

maioridade = 0
menoridade = 0

for c in range(1,8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = ano_atual - nascimento
    if idade > 18:
        maioridade += 1
    else:
        menoridade += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maioridade))
print('E também tivemos {} menores de idade'.format(menoridade))

    
    