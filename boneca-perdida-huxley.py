def main():
    T = int(input())  # número de casos de teste

    for _ in range(T):
        N = int(input())  # quantidade de bonecas
        dolls = []

        for _ in range(N):
            doll_type = int(input())  # tipo de boneca
            dolls.append(doll_type)

        missing_doll = find_missing_doll(dolls)
        print(missing_doll)


def find_missing_doll(dolls):
    count = {}  # dicionário para contar a ocorrência de cada tipo de boneca

    # Conta a ocorrência de cada tipo de boneca
    for doll in dolls:
        if doll in count:
            count[doll] += 1
        else:
            count[doll] = 1

    # Encontra o tipo de boneca que ocorre em número ímpar
    for doll, occurrence in count.items():
        if occurrence % 2 == 1:
            return doll

    return None  # retorna None se todas as bonecas possuem pares


if __name__ == "__main__":
    main()
