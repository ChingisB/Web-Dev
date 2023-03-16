if __name__ == '__main__':
    data = []
    values = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
        values.add(score)
    second_lowest = sorted(list(set(map(lambda x: x[1], data))))[1]
    answers = []
    for name, point in data:
        if point == second_lowest:
            answers.append(name)
    print(*sorted(answers), sep='\n')   