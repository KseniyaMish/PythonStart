A = {}
a = {}
count = 0

total_count = int(input())

for i in range(total_count):
    line = input().strip().split(';')
    first = line[0]
    second = line[2]

    if first not in A:
        A[first] = [0, 0, 0, 0, 0]
    if second not in A:
        A[second] = [0, 0, 0, 0, 0]

    A[first][0] += 1  # количество сыгранных игр
    A[second][0] += 1  # количество сыгранных игр

    if int(line[1]) > int(line[3]):
        A[first][1] += 1  # количество выигранных игр
        A[second][3] += 1  # количество проигранных игр
        A[first][4] += 3  # получает баллов
    elif int(line[1]) == int(line[3]):
        A[first][2] += 1  # количество ничьей
        A[second][2] += 1  # количество ничьей
        A[first][4] += 1  # получает баллов
        A[second][4] += 1  # получает баллов
    else:
        A[first][3] += 1  # количество проигранных игр
        A[second][1] += 1  # количество выигранных игр
        A[second][4] += 3  # получает баллов

for m in A:
    print(m + ':' + ' '.join(str(x) for x in A[m]))