# пузырьковая сортировка

mas = [7, 2, 9, 4, 8, 6, 1, 5, 3, 10]
n = 9
for i in range(n - 1):
    for i in range(n - i - 1):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]


print(mas)
