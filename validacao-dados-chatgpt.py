def ler_sexo():
    while True:
        sexo = input("Digite o sexo (M/F): ")
        if sexo.upper() == 'M' or sexo.upper() == 'F':
            return sexo.upper()
        else:
            print("Valor incorreto. Digite 'M' para masculino ou 'F' para feminino.")

# Chamada da função para ler o sexo
sexo_pessoa = ler_sexo()
print("Sexo digitado:", sexo_pessoa)
