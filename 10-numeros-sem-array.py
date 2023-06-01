def contar_numero(n, numeros):
    count = 0
    for num in numeros:
        if num == n:
            count += 1
    return count

def main():
    while True:
        n = int(input("Digite o número a ser procurado (-1 para sair): "))
        if n == -1:
            break
        
        numeros = []
        for _ in range(1000):
            num = int(input())
            numeros.append(num)
        
        count = contar_numero(n, numeros)
        print(f"{n} appeared {count} times")

if __name__ == '__main__':
    main()
