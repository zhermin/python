
name = input("enter name")
cash = "$" + str(110)


h = open ("Highscores.txt", "a")
h.write((name + " | " + str(cash)).center(77))
h.write("\n")
h.close()

h = open("Highscores.txt")
content = h.read()
h.close()
print(content)
