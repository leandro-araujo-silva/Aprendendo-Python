def count_interpretations(L, D, N, words, patterns):
    result = []
    for i in range(N):
        pattern = patterns[i]
        count = 0
        for word in words:
            if match_pattern(word, pattern):
                count += 1
        result.append(count)
    return result

def match_pattern(word, pattern):
    stack = []
    index = 0
    for char in pattern:
        if char == '(':
            stack.append([])
        elif char == ')':
            options = stack.pop()
            if word[index] not in options:
                return False
            index += 1
        else:
            if char != word[index]:
                return False
            index += 1
    return True

def main():
    T = int(input())
    for case in range(1, T+1):
        L, D, N = map(int, input().split())
        words = []
        patterns = []
        for _ in range(D):
            words.append(input().strip())
        for _ in range(N):
            patterns.append(input().strip())
        interpretations = count_interpretations(L, D, N, words, patterns)
        for i, count in enumerate(interpretations):
            print("Caso #{}: {}".format(i+1, count))

if __name__ == "__main__":
    main()





