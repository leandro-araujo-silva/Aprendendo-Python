def last_ordered_number(n):
    # Converter o número de entrada para uma lista de dígitos
    digits = list(str(n))
    
    # Percorrer a lista de dígitos da direita para a esquerda
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            # Se o dígito atual for menor que o anterior,
            # decrementar o dígito anterior e ajustar os dígitos à direita para 9
            digits[i - 1] = str(int(digits[i - 1]) - 1)
            digits[i:] = ['9'] * (len(digits) - i)
    
    # Construir o número ordenado a partir da lista de dígitos
    last_number = int(''.join(digits))
    
    return last_number

def main():
    t = int(input())  # Número de casos de teste

    for i in range(1, t + 1):
        n = int(input())  # Último número contado para o caso de teste
        result = last_ordered_number(n)
        print(f"Caso #{i}: {result}")

main()
