def power(base, pwr):
	res = 1
	for i in range(pwr):
		res = res * base
	return res


grid = [
	[["a1", "a2"], ["b1", "b2"], ["c1", "c2"]],
	[["d1", "d2"], ["e1", "e2"], ["f1", "f2"]],
]


for a in grid:
	for b in a:
		for c in b:
			c = c


class Student:
	def __init__(self, name, major, gpa, is_on_probation):
		self.name = name
		self.major = major
		self.gpa = gpa
		self.prob = is_on_probation

	def honour(self):
		if self.gpa >= 3.5:
			return True
		else:
			return False

	def add_score(self):
		if self.major == "Art":
			self.gpa += 1

	def x_score(self, multiplier):
		return self.gpa * multiplier