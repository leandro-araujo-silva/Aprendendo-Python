# Função para encontrar a boneca sem par
def encontrar_boneca_sem_par(bonecas):
    bonecas_sem_par = set()

    for boneca in bonecas:
        if boneca in bonecas_sem_par:
            bonecas_sem_par.remove(boneca)
        else:
            bonecas_sem_par.add(boneca)

    return bonecas_sem_par.pop()

# Entrada de dados
T = int(input(""))

for _ in range(T):
    N = int(input(""))

    bonecas = []
    for _ in range(N):
        boneca = input("")
        bonecas.append(boneca)

    # Chama a função para encontrar a boneca sem par
    boneca_sem_par = encontrar_boneca_sem_par(bonecas)

    # Imprime o tipo da boneca sem par
    print(boneca_sem_par)
