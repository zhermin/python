# SCISSORS PAPER STONE

print("A simple scissors paper stone game created by Zher Min")
print("Note: All answers have to be in small letters")
print("")


import random


# Point System

class Points:

    def __init__(self):
        self.myScore = 0
        self.oppScore = 0
    
    def win(self):
        print("")
        print("You win!")
        self.myScore += 1

    def lose(self):
        print("")
        print("You lose!")
        self.oppScore += 1

    def checkScores(self):       
        print("")
        print("You - Python : " + str(self.myScore) + " - " + str(self.oppScore))
        print("")

scores = Points()

    
def play():


    # Choices

    choices = ["scissors", "paper", "stone"]


    # Player

    print("Scissors, paper, stone!")
    print("")
    print("You choose ", end="")
    player = input()
    while player not in choices:
        print("Invalid choice")
        print("You choose ", end="")
        player = input()


    # Opponent

    opponent = random.choice(choices)
    print("Your opponent chose " + opponent + "!")
    print("")


    # Results

    if player == opponent:
        print("It's a draw!")
    elif player == choices[0] and opponent == choices[1]:
        print("Scissors beat paper!")
        scores.win()
    elif player == choices[1] and opponent == choices[2]:
        print("Paper beats stone!")
        scores.win()
    elif player == choices[2] and opponent == choices[0]:
        print("Stone beats scissors!")
        scores.win()
    elif player == choices[0] and opponent == choices[2]:
        print("Stone beats scissors!")
        scores.lose()        
    elif player == choices[1] and opponent == choices[0]:
        print("Scissors beat paper!")
        scores.lose()
    elif player == choices[2] and opponent == choices[1]:
        print("Paper beats stone!")
        scores.lose()
    scores.checkScores()            
    replay()

    # Replay

def replay():
    while True:
        play_again = input("Press enter to play again >>> ")
        if play_again == "":
            play()
        else:
            print("")
            print("I don't know what you wrote but thanks for playing!")
            print("")

            


play()
