import numpy as np
import matplotlib.pyplot as plt

"""

dick = {"Cash" : "$200"}
dick ["newkey"] = "newvalue"
dick ["newnewkey"] = "newnewvalue"

#print ("@" * 80)

lizt = ["f", "r", "x", "s"]
lizt.append ("e")
lizt.sort()
#print (lizt)

#print (lizt[1])
#for x in lizt:
    #print(x)

#print("Results for the dog show are as follows:\n")
for index, x in enumerate(lizt):
    place = str(index)


#for i in lizt:
    #print ("no. " + i) 

"""

"""
	
hist = []

pft = 85
cash = hist.append(float(input("Cash? ")))
whack = hist.append(float(20))
expft = hist.append(float(17))
rslt = hist.append(0)
fpft = hist.append(float(-20))
fcash = hist.append(float(80))


#for a in hist:
    #print ("Cash = $" + str(a))

	
#print ("Cash		Whack		XPft		W/L	FPft	FCash")
#print (str(hist[0]) + "		" + str(hist[1]) + "	" + str(hist[2]) + "	" + str(hist[3]) + "	" + str(hist[4]) + "	" + str(hist[5]))
	

	
print (("-|" * 14) + "HISTORY | %PROFITS = " + str(pft) + "%" + ("-|" * 14))

print (
"Cash" + (" " * (14-len("Cash")))
+ "Whack" + (" " * (15-len("Whack")))
+ "XPft" + (" " * (14-len("XPft")))
+ "W/L" + (" " * (7-len("W/L")))
+ "FPft" + (" " * (14-len("FPft")))
+ "FCash" + (" " * (15-len("FCash")))
)

print (
"$" + str(hist[0]) + (" " * (14-1-len(str(hist[0]))))
+ "$" + str(hist[1]) + (" " * (15-1-len(str(hist[1]))))
+ "$" + str(hist[2]) + (" " * (14-1-len(str(hist[2]))))
+ str(hist[3]) + (" " * (7-len(str(hist[3]))))
+ "$" + str(hist[4]) + (" " * (14-1-len(str(hist[4]))))
+ "$" + str(hist[5]) + (" " * (15-1-len(str(hist[5]))))
)

input ()

"""

"""

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()

"""

"""

all_items = []
new_item = {}
for i in range(0,5):
    print (new_item)
    new_item['a'] = i
    new_item['b'] = i

    print (new_item)
    
    all_items.append(new_item)
    print (all_items)
    print (hex(id(new_item)))  # print memory address of new_item

print (all_items)
input()




all_items = []
for i in range(0,5):
    new_item = {}
    new_item['a'] = i
    new_item['b'] = i

    all_items.append(new_item)
    print (new_item)


print (all_items)

"""


hist_1 = open("test.txt", "w+")
hist_1.write ("CASH		WHACK\n")
hist_1.close ()

hist_1 = open("test.txt", "a")
for i in range(5):
     hist_1.write("Appended line %d\r\n" % (i+1))

hist_1.close ()

hist_1 = open("test.txt", "r")
content = hist_1.read()
print (content)
input ()