
mas = [1, 2, 3, 4, -5, -6]
print(*mas, sep=', ')

mas_l = 0
cykle = 0
while cykle <= 10:
    try:
        if mas[cykle] >= 0:
             mas_l += 1
        cykle += 1
    except:
        cykle += 100

print(mas_l)