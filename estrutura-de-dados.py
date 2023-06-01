def push(pilha, numeros):
    pilha.append(numeros)

def pop(pilha):
    if not pilha:
        print("EMPTY STACK")
    else:
        numeros = pilha.pop()
        print(numeros)

# Função principal
def main():
    pilha = []

    while True:
        comando = input().strip().upper()

        if comando == "PUSH":
            numeros = list(map(int, input().split()))
            push(pilha, numeros)
        elif comando == "POP":
            pop(pilha)
        else:
            break

# Executar a função principal
main()
