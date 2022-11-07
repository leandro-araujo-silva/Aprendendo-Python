l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if (l1 == l2 and l1 == l3):
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif (l1 != l2 and l1 != l3 and l2 != l3):
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
    else: 
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
else: 
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

