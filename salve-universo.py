def main():
    T = int(input())  # número de casos de teste

    for case in range(1, T + 1):
        S = int(input())  # número de motores de busca
        engines = []
        for _ in range(S):
            engines.append(input())  # nome dos motores de busca

        Q = int(input())  # número de consultas
        queries = []
        for _ in range(Q):
            queries.append(input())  # consultas

        switches = 0
        current_engine = engines[0]  # começa com o primeiro motor de busca

        for query in queries:
            if query == current_engine:  # se a consulta é igual ao motor de busca atual, precisa alternar
                switches += 1
                current_engine = next_engine(current_engine, engines, query)  # encontra o próximo motor de busca disponível

        print(f"Caso #{case}: {switches}")


def next_engine(current, engines, query):
    # encontra o próximo motor de busca disponível, ignorando o atual e a consulta atual
    for engine in engines:
        if engine != current and engine != query:
            return engine

    return current  # se não houver outro motor de busca disponível, retorna o motor de busca atual


if __name__ == "__main__":
    main()
