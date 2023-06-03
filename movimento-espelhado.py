# Função para espelhar as coordenadas
def espelhar_coordenadas(lado, coordenadas):
    coordenadas_espelhadas = []

    for coord in coordenadas:
        linha, coluna = coord
        coluna_espelhada = lado - coluna + 1
        coordenada_espelhada = (linha, coluna_espelhada)
        coordenadas_espelhadas.append(coordenada_espelhada)

    return coordenadas_espelhadas

# Entrada de dados
lado = int(input())
coordenadas = eval(input())

# Chamada da função para espelhar as coordenadas
coordenadas_espelhadas = espelhar_coordenadas(lado, coordenadas)

# Construção da saída sem espaços entre os números de cada parênteses
saida = ",".join(["({},{})".format(linha, coluna) for linha, coluna in coordenadas_espelhadas])
print(saida)
