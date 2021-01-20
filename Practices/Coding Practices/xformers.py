class JoinableTransformer(object):
    def __init__(self, n):
        # Your code here
        return
    def get_brother(self, k):
	# Your code here
        return
    def join(self, b):
        # Your code here
        return
    def separate(self):
        # Your code here
        return
    def fight(self, b):
	# Your code here
        return
      
######################################################################
######################################################################
######### DO NOT MODIFY ANYTHING BELOW ###############################
######################################################################
######################################################################

# These are the evil Decepticon Constructicons - they can combine into
# this nasty giant Decepticon called Devastator
overload = JoinableTransformer(5)
mixmaster = overload.get_brother(2)
longhaul = overload.get_brother(3)
rampage = overload.get_brother(4)
scrapper = overload.get_brother(5)
scrapper2 = overload.get_brother(5)
print(scrapper is scrapper2) # => True
print(scrapper is longhaul) # => False

print("-----------------------")
# These are the small Autobot twins - they can combine into a pink and
# white ice cream van
mudflap = JoinableTransformer(2)
skids = mudflap.get_brother(2)
print(mudflap.join(rampage))  # => "Can't join"
print(mudflap.join(mudflap))  # => "Can't join"
print(mudflap.fight(rampage)) # => "Fight ends in draw"

print("-----------------------")
# Let's get some help!
print(mudflap.join(skids))    # => "Transformers joined"
print(mudflap.fight(rampage)) # => "Fight won"
print(skids.fight(rampage))   # => "Fight won"

print("-----------------------")

# Twins had a fight :-(
print(mudflap.separate())     # => "Transformers separated"
print(skids.separate())       # => "Not joined"

print("-----------------------")

print(mudflap.fight(rampage)) # => "Fight ends in draw"
print(skids.fight(rampage))   # => "Fight ends in draw"
print(rampage.fight(skids))   # => "Fight ends in draw"

print(rampage.join(scrapper)) # => "Transformer joined"
print(mudflap.fight(rampage)) # => "Fight lost"

# Brother to the rescue!
print(skids.join(mudflap))    # => "Transformers joined"
print(mudflap.fight(rampage)) # => "Fight ends in draw"

# Let's bully the small one
print(skids.fight(longhaul))  # => "Fight won"

# Oh no, they're getting bigger!
print(scrapper.join(longhaul))# => "Transformers joined"
print(skids.fight(longhaul))  # => "Fight lost"

# Bad guys falling apart!
print(rampage.separate())    # => "Transformers separated"

# Things are getting better!
print(mudflap.fight(longhaul))    # => "Fight ends in a draw"

# Bad guys falling apart!
print(scrapper.separate())    # => "Transformers separated"

# 0wn3d!
print(mudflap.fight(longhaul)) # => "Fight won"

