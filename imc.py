peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sual altura? (m) '))

imc = peso / (altura * altura)

print('O seu IMC é de {:.2f}.'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Parabéns, você está no peso ideal')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Parabéns, você está obeso.')
else:
    print('Alerta, você está com obesidade mórbida.')