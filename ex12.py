
mas = [168, 167, 165, 164, 163, 160]
print(*mas, sep=', ')

num = int(input("Ваше число: ")) # 166

x = 0 
while x < 100:
	try:
		if num > mas[x]:
			print(f"Позиция: {x+1}")
			x += 100
	except:
		pass
	x += 1