from pwr1 import Student
from questions import Q

s1 = Student("Jim", "Business", 3.1, False)
s2 = Student("Jake", "Art", 2.9, True)

s2.add_score()
s1.add_score()

'''
print(str(s2.gpa) + " and " + str(s1.gpa))
print(s2.x_score(s1.gpa))
'''


Q.prompt = [
    "q1.\n(a)\n(b)\n(c)\n\n",
    "q2.\n(a)\n(b)\n(c)\n\n",
    "q3.\n(a)\n(b)\n(c)\n\n",
]

thequestions = [
    Q(Q.prompt[0], "a"),
    Q(Q.prompt[1], "c"),
    Q(Q.prompt[2], "b")
]

def run_test(whatarethequestions):
    score = 0
    for Q in thequestions:
        answer = input(Q.prompt)
        if answer == Q.answer:
            score += 1
    print(str(score) + "/" + str(len(thequestions)))

