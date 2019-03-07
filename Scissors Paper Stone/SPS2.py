# SCISSORS PAPER STONE

import random



# Choices

choices = ["scissors", "paper", "stone"]



# Player

player = input()
def step2():
    print("Scissors, paper, stone!")
    print("")
    print("You choose ", end="")
    player = input()
    while player not in choices:
        print("Invalid choice")
        print("You choose ", end="")
        player = input ()



# Opponent

def step3():
    opponent = random.choice(choices)
    print("Your opponent chose " + opponent + "!")
    print("")



# Results

def step4():
    if player == opponent:
        print("It's a draw!")
    elif player == choices[0] and opponent == choices[1]:
        print("Scissors beat paper! You win!")
    elif player == choices[0] and opponent == choices[2]:
        print("Stone beats scissors! You lose!")
    elif player == choices[1] and opponent == choices[2]:
        print("Paper beats stone! You lose!")
    elif player == choices[1] and opponent == choices[0]:
        print("Scissors beat paper! You lose!")
    elif player == choices[2] and opponent == choices[1]:
        print("Paper beats stone! You lose!")
    elif player == choices[2] and opponent == choices[0]:
        print("Stone beats scissors! You win!")



# Replay
def step5():
    playAgain = "yes"
    while playAgain == "yes":
        step2()
        step3()
        step4()
        step5()
        playAgain = input()


step2()
step3()
step4()
step5()

