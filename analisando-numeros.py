number = int(input('Digite um número: '))
milhar = number // 1000
cent = (number % 1000) // 100
dez = (number % 100) // 10
unid = (number % 100) % 10
print("Milhar: {}".format(milhar))
print("Centena: {}".format(cent))
print("Dezena: {}".format(dez))
print("Unidade: {}".format(unid))