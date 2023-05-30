soma = 0
homemVelho = 0
Nhomemmaisvelho = ''
novinha = 0

for c in range(1,5):
    print("--------------{}° PESSOA--------------".format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    soma += idade 
    if sexo == "M" or sexo == "m":
        if idade > homemVelho:
            homemVelho = idade
            Nhomemmaisvelho = nome
    if (sexo == "F" or sexo == "f") and idade < 20:
        novinha += 1
media = soma / 4

print('A média de idade do grupo é de {:.2f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(homemVelho, Nhomemmaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(novinha))
