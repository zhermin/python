# Joinable Transformers
# Decepticons : overload, mixmaster, longhaul, rampage, scrapper
# Autobots : mudflap, skids

# class CreateFamily():

#     def __init__(self):

class JoinableTransformers():

    def __init__(self, n):

        self.n = n
        self.originalbro = 1
        self.brotherlist = []

        for i in range(1, n+1):
            self.brotherlist.append(i)

        

    def get_brother(self, k): # original joining with k

        return

overload = JoinableTransformers(5)
#mixmaster = overload.get_brother(2)

print(overload.brotherlist)