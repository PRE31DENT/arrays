
mas = [1, 2, 3, 4, 4, 6]
print(*mas, sep=', ')
mas_back = [] # Обратный список

for x in mas:
    try:
        mas_back.insert(0, mas[x-1])
    except:
        pass

print(*mas_back, sep=', ')