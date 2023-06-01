def main():
    numeros = []
    for _ in range(3):
        num = int(input(" "))
        numeros.append(num)
    
    numeros_ordenados = sorted(numeros)
    for num in numeros_ordenados:
        print(num)

if __name__ == '__main__':
    main()
