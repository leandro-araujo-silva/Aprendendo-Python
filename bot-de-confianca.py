def main():
    T = int(input())

    for case in range(1, T + 1):
        N, *buttons = input().split()
        N = int(N)
        orange_buttons = set()
        blue_buttons = set()
        orange_time = 0
        blue_time = 0

        for i in range(0, N * 2, 2):
            robot = buttons[i]
            position = int(buttons[i + 1])

            if robot == 'O':
                if position in blue_buttons:
                    orange_time += 1
                    blue_buttons.remove(position)
                else:
                    orange_time = max(orange_time + 1, blue_time + 1)
                orange_buttons.add(position)
            elif robot == 'B':
                if position in orange_buttons:
                    blue_time += 1
                    orange_buttons.remove(position)
                else:
                    blue_time = max(blue_time + 1, orange_time + 1)
                blue_buttons.add(position)

        result = max(orange_time, blue_time)
        print(f"Caso #{case}: {result}")


if __name__ == "__main__":
    main()




