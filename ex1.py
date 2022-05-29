
mas = [1, 2, 3, 4, 5, 6]
print(*mas, sep=', ')

mas_l = []

for x in mas:
    if mas.index(x) % 2 == 0:
        mas_l.append(mas[x-1])

print(*mas_l, sep=', ')