import random
import pandas as pd

class RandomCaption:

    def __init__(self):

        print("Reading the CSV File [hashlist.csv]..")
        df = pd.read_csv("hashlist.csv")

        generalTags = df[df.category == "general"].sample(10)
        poetryTags = df[df.category == "poetry"].sample(10)
        motivationTags = df[df.category == "motivation"].sample(10)

        self.captionDF = pd.concat([generalTags, poetryTags, motivationTags])

    def getCaption(self):

        print("Churning out 30 Random Hashtags..")
        tempList = []

        for row in self.captionDF.iterrows():
            index, data = row
            tempList.append(data.tolist())

        finalCaption = []
        for i in range(len(tempList)):
            finalCaption.append(tempList[i][0])

        random.shuffle(finalCaption)

        return " ".join(finalCaption)

if __name__ == "__main__":
    print(RandomCaption().getCaption())