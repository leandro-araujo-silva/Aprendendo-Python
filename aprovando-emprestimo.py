valorCasa = float(input('Valor da casa: R$ '))
salarioComprador = float(input('Salário do comprador: R$ '))
financiamento = int(input('Quantos anos de financiamento? '))
financiamentoMeses = financiamento * 12
valorMensal = valorCasa / financiamentoMeses
aprovacaoEmprestimo = (valorMensal / salarioComprador) * 100

print('Para pagar uma casa de R$ {} em {} anos a prestaçao será de R$ {:.2f}'.format(valorCasa, financiamento, valorMensal))

if aprovacaoEmprestimo > 30:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
