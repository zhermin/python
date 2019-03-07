# SCISSORS PAPER STONE

import random


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
        player = input ()



    # Opponent

    opponent = random.choice(choices)
    print("Your opponent chose " + opponent + "!")
    print("")



    # Results

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

    
    replay()



# Replay

def replay():
    while True:
        play_again = input("Would you like to play again? (yes/no) > ")
        if play_again == "yes":
            play()
        if play_again == "no":
            print("Thanks for playing!")
        else:
            print("")
            print("I'm sorry I could not recognize what you entered")
            print("")

            
play()

