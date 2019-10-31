import random
rocklist = ["rock","paper", "scissors"]

def get_yn(prompt):
    play = input(str(prompt) + " (y/n) ")
    first = play[0]
    play = first.lower()
    return play

def userinput():
    while True:
        user = input("Rock, Paper, Scissors?")
        user = user.lower()
        if user in rocklist:
            return rocklist.index(user)
        else:
            print("Bad Input. Please type from list")

def compare(user, com):
    if user == 0:
        if com == 0:
            return "tie"
        elif com == 1:
            return("com")
        elif com == 2:
            return "user"
    elif user == 1:
        if com == 0:
            return "user"
        elif com == 1:
            return "tie"
        elif com == 2:
            return "com"
    elif user == 2:
        if com == 0:
            return "com"
        elif com == 1:
            return "user"
        elif com == 2:
            return "tie"

def playGame():
    user = userinput()
    print("User Chose: " + rocklist[user] )
    com = random.randrange(0,3,1)
    print("Com Chose: " + rocklist[com] )
    return compare(user, com)


def playGameLoop():
    print("welcome to RPS")

    play = get_yn("Play a round of RPS?")


    while play == "y" :
        winner = playGame()
        print("winner: " + winner)
        play = get_yn("Play RPS again?")


playGameLoop()