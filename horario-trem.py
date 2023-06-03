def main():
    T = int(input())  # Número de casos de teste

    for case in range(1, T + 1):
        TATime = int(input())  # Tempo de retorno em minutos
        NA, NB = map(int, input().split())  # Número de viagens de A para B e de B para A

        departures_A = []
        arrivals_A = []
        departures_B = []
        arrivals_B = []

        for _ in range(NA):
            departure, arrival = input().split()
            departures_A.append(convert_to_minutes(departure))
            arrivals_B.append(convert_to_minutes(arrival))

        for _ in range(NB):
            departure, arrival = input().split()
            departures_B.append(convert_to_minutes(departure))
            arrivals_A.append(convert_to_minutes(arrival))

        departures_A.sort()
        arrivals_A.sort()
        departures_B.sort()
        arrivals_B.sort()

        trains_A = calculate_trains_required(departures_A, arrivals_B, TATime)
        trains_B = calculate_trains_required(departures_B, arrivals_A, TATime)

        print(f"Case #{case}: {trains_A} {trains_B}")


def convert_to_minutes(time):
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def calculate_trains_required(departures, arrivals, TATime):
    trains = 0
    max_trains = 0

    for departure in departures:
        i = 0
        while i < len(arrivals) and arrivals[i] <= departure:
            i += 1

        j = i
        while j < len(arrivals) and arrivals[j] < departure + TATime:
            j += 1

        trains += 1
        max_trains = max(max_trains, trains)

        if i == j:
            trains -= 1

    return max_trains


if __name__ == "__main__":
    main()

