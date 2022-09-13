frase = '    curso em video python'
print(frase.upper())
print(frase.strip())
print(frase.upper().strip())
print(frase.strip().capitalize())
newFrase = frase.strip()
print(newFrase)
print('-'.join(newFrase.split()))
print(newFrase.replace('python', 'Android'))


palavra = 'Bom dia mundo'
dividido = palavra.split()
print(dividido[1][1])