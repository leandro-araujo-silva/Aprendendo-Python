# Função para verificar o estado da lâmpada após K estalos de dedos
def verificar_estado_lampada(N, K):
    # Verificar se o número de estalos de dedos é múltiplo de 2^N
    if K % (2 ** N) == (2 ** N) - 1:
        return "ON"
    else:
        return "OFF"

# Entrada de dados
T = int(input())

# Processamento e saída
for caso in range(1, T + 1):
    N, K = map(int, input().split())
    estado_lampada = verificar_estado_lampada(N, K)
    print(f"Caso #{caso}: {estado_lampada}")
