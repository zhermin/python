for i in range (100):

	i += 1
	a = "Fizz"
	b = "Buzz"

	if i % 3 == 0 and i % 5 == 0:
		print(a+b)
		continue

	elif i % 3 == 0:
		print(a)

	elif i % 5 == 0:
		print(b)

	else:
		print(i)

input("Done")