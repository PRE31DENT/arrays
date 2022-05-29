
mas = [1, 2, 3, 5, 3, 8, 9]
print(*mas, sep=', ')
mas_back = []


c = 0
while c < 1000:
    try:
        mas_back.append(mas[c+1])
        mas_back.append(mas[c])
    except:
       try:
           mas_back.append(mas[c])
       except:
           pass
    c += 2

print(*mas_back, sep=', ')