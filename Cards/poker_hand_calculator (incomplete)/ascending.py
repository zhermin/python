

def compare(sortb):

	for i in range (len(sortb) - 4):

		strt = 0

		for x in range(4):

			print(sortb[i], sortb[i + x + 1])
			if sortb[i] + x + 1 == sortb[i + x + 1]:
				strt += 1

		if strt == 4:
			print("straight draw!")


#b =[0, 1, 2, 3, 4, 5, 6]
b = [11, 13, 6, 5, 3, 4, 7, 8, 9]
sortb = sorted(b)
print(sortb)
compare(sortb)
input()