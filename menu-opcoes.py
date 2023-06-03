opcao = -1

v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))

while opcao != 5:

    print("""
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
    """)
    escolha = int(input('Qual é a sua opção? ')) 
    opcao = escolha
    
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}'.format(v1, v2, soma))
    elif opcao == 2:
        multiplicar = v1 * v2        
        print('O resultado de {} x {} é {}'.format(v1, v2, multiplicar))
    elif opcao == 3:
        if v1 > v2:
            print('Entre {} e {} o maior é {}'.format(v1, v2, v1))
        elif v1 < v2:
            print('Entre {} e {} o maior é {}'.format(v1, v2, v2))
        else:
            print('Os dois valores são iguais!')
    elif opcao == 4:
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        print('Fim do programa.')
    else:
        print('Opção inválida. Tente novamente!')
        



