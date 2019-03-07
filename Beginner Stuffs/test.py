x = 20
while x > 0:
    print (x)
    if x > 5:
        print ("Big number!")
    elif x % 2 != 0:
        print ("This is an odd number")
        print ("It isn't greater than five, either")
    else:
        print ("This number isn't greater than 5")
        print ("but is an even number")
        print ("feeling confused?")
    x = x - 1
    print ("We've just made 'x' one less than what it was!")
    print ("And unless x is not greater than 0, we'll do the loop again.")
print ("Well, it seems as if 'x' is now no longer bigger than 0!")
print ("the loop is now over, and without furthur ado, so is this program!")

#basically, first step = set x equals 10
#secondly, set a loop "while" for every instance in which x is above 0
#next, if x is above 5, it will print "big number"
#or else, if x is NOT even (giving no remainder when divided by 2)
#nor is it greater than 5 (ELSE to the first check of "IF x is more than 5",
#then it will print,
#"this is an odd number" and that "it isn't greater than 5 either"
#IF however, the ELIF instruction is true, where
#x is even, nor is it greater than 5 (ELSE to the very first check)
#then it will print that bunch of lines
#finally, after everything have been checked, the line x = x - 1
#will give the original x a new value
#this loop of x reducing by 1 will repeat until x is not more than 0
#in other words, x = 0
