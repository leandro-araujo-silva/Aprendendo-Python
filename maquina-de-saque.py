# Função para determinar se cada pessoa receberá a quantia necessária de dinheiro
def determinar_retiradas_pessoas(N, K, valores):
    total_dinheiro = K
    retiradas = [0] * N

    for i in range(N):
        if total_dinheiro >= valores[i]:
            retiradas[i] = 1
            total_dinheiro -= valores[i]

    return retiradas

# Entrada de dados
T = int(input("Digite o número de casos de teste: "))

for _ in range(T):
    N, K = map(int, input("Digite a quantidade de pessoas e o total de dinheiro disponível: ").split(","))

    valores = list(map(int, input("Digite a quantia que cada pessoa tenta sacar: ").strip("()").split(",")))

    # Chama a função para determinar as retiradas das pessoas
    retiradas = determinar_retiradas_pessoas(N, K, valores)

    # Imprime o resultado
    resultado = ''.join(str(retirada) for retirada in retiradas)
    print(resultado)
