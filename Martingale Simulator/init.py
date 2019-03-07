i = input("Global i? ")

class Class(object):
	
	i = input ("Class i? ")
	
	def __init__(self):
		self.i = input ("init i? ")
		self.x = self.i

init = Class()


print ("Global i = " + i)
input ()

print ("Class i = " + Class.i + init.x)
input ()

print ("init i = " + init.i)
input ()

if Class.i > init.i:
	print ("Class > init")
	input ()