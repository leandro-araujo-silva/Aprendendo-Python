velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
  multa = (velocidade - 80) * 7
  print('MULTADO! Você excedeu o limite que é de 80Km/h')
  print('Você deve pagar uma multa de R${}!'.format(multa))
  print('Tenha um bom dia! Dirija com segurança!')
else:
  print('Tenha um bom dia! Dirija com segurança!')