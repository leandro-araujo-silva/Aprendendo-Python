def verificar_palindromo(palavra):
    # Remover espaços em branco e converter para letras minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Verificar se a palavra é igual à sua inversão
    if palavra == palavra[::-1]:
        return True
    else:
        return False

# Exemplos de palavras para verificar
palavra1 = "radar"
palavra2 = "Python"
palavra3 = "socorram me subi no onibus em marrocos"

# Verificar se as palavras são palíndromos
print(verificar_palindromo(palavra1))  # Saída: True
print(verificar_palindromo(palavra2))  # Saída: False
print(verificar_palindromo(palavra3))  # Saída: True
