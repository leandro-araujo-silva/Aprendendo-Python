compras = float(input('Preço das compras: R$ '))

print('''
Formas de pagamento
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão 
''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    gasto = compras * 0.9
    print('Apesar de sua compra ser de {}, você pagará R$ {}'.format(compras, gasto))
elif opcao == 2:
    gasto = compras * 0.95
    print('Apesar de sua compra ser de {}, você pagará R$ {}'.format(compras, gasto))
elif opcao == 3:
    print('Você pagará R$ {}'.format(compras))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    gasto = compras * 1.2
    valParcelas = gasto / parcelas

    print('Sua compra será parcelada em {}x de R${} com juros.'.format(parcelas, valParcelas))
    print('Apesar de sua compra ser de {}, você pagará R$ {}'.format(compras, gasto))
else:
    print('Opção inválida!')