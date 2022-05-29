
mas = [1, 2, 3, 5, 8, 6]
print(*mas, sep=', ')

yn = 0
for x in mas:
    try:
        if mas[x-1] == mas[x]:
            yn = 1
    except:
        pass

if yn == 0:
    print("NO")
else:
    print("YES")