distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
  print('E o preço da sua passagem será de {}'.format(distancia * 0.5))
else:
   print('E o preço da sua passagem será de R${}'.format(distancia * 0.45))