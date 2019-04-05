import random
import pandas as pd

df = pd.read_csv("hashlist.csv")

partOne = df[df.category == "general"].sample(15)
partTwo = df[df.category == "poetry"].sample(15)

captionDF = pd.concat([partOne, partTwo])

tempList = []

for row in captionDF.iterrows():
    index, data = row
    tempList.append(data.tolist())

finalCaption = []
for i in range(len(tempList)):
    finalCaption.append(tempList[i][0])

random.shuffle(finalCaption)

print(finalCaption)