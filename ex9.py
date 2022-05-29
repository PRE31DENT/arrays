
mas = [1, 2, 3, 5, 3, 8, 9]
print(*mas, sep=', ')

mas.insert(0, mas[-1])
mas.pop()

print(*mas, sep=', ')