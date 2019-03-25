import matplotlib.pyplot as plt

# Line Chart
# x = [1,2,3]
# y = [4,9,2]

# x2 = [1,2,3]
# y2 = [10,18,12]

# plt.plot(x,y, label="First Line")
# plt.plot(x2,y2, label="Second Line")


# Bar Chart
# x = [2,4,6,8,10]
# y = [6,7,8,2,4]

# x2 = [1,3,5,7,9]
# y2 = [7,8,3,6,1]

# plt.bar(x,y, label="Bars 1")
# plt.bar(x2,y2, label="Bars 2")


# Histograms
# population_ages = [22,44,52,2,75,84,42,61,35,72,102,120,14,18,42,36,71,24,24,61,24,7,2,63,24,52,46,62,13,21,124,128,101]

# ids if wanted to do bar graph
# ids = [x for x in range(len(population_ages))]

# bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
# plt.hist(population_ages, bins, histtype="bar", rwidth=0.8, label="Ages")


# Scatter Graph
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [4,7,8,1,14,25,3,26,32,40]

# plt.scatter(x,y, label="Scatter", color="k", marker="x")


# Stack Plots / Pie Charts
days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]

slices = [7,2,2,13]

activities = ["Sleeping","Eating","Working","Playing"]

# plt.stackplot(days, sleeping,eating,working,playing, labels=activities)
plt.pie(slices,
        labels=activities,
        startangle=90,
        explode=(0,0,0.1,0),
        autopct="%1.1f%%"
)



# plt.xlabel("x label here")
# plt.ylabel("y label here")

plt.title("Graphing Tutorial")
# plt.legend()
plt.show()