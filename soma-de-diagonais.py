# Função para realizar a soma das diagonais
def soma_diagonais(matriz1, matriz2):
    tamanho = len(matriz1)
    soma = 0

    # Soma os elementos da diagonal principal da matriz1
    for i in range(tamanho):
        soma += matriz1[i][i]

    # Soma os elementos da diagonal principal da matriz2 rotacionada 90 graus para a direita
    for i in range(tamanho):
        soma += matriz2[i][tamanho-1-i]

    return soma

# Entrada de dados
print("Digite a primeira matriz:")
matriz1 = eval(input())

print("Digite a segunda matriz:")
matriz2 = eval(input())

# Chama a função para realizar a soma das diagonais
resultado = soma_diagonais(matriz1, matriz2)

# Imprime o resultado
print("A soma das diagonais é:", resultado)
