import time  # import time to sleep some times
import random  # import random to select random objects


def print_pause(message):
    print(message)
    time.sleep(2)


# beggining
def startGame():
    chances = random.randint(0, 1)
    if (chances == 0):
        print_pause("you find yourself in a Desert.")
        print_pause("you have to cross it, and make it to the exit.")
        print_pause("will you make it?")
    else:
        print_pause("you find yourself in a Forest.")
        print_pause("you have to cross it, and reach to the sea.")
        print_pause("your way is unknown!")
    askForInput("fight", "run")


# continue
def askForInput(opt1, opt2):
    print_pause("you find monsters in your way.")
    while True:
        response = input("what do you want to do? " + opt1 + " or " + opt2)
        if (opt1 == response):
            fight()
            break
        elif (opt2 == response):
            run()
            break
        else:
            print_pause("wrong choice, please select from options only")


# user choice
def fight():
    print_pause("you fought the monsters, you killed them!")
    print_pause("you win!")
    print_pause("Game Over.")
    playAgain()


def run():
    print_pause("you run away and monsters caught you, and killed you.")
    print_pause("you lost!")
    print_pause("Game Over.")
    playAgain()


# restart the game
def playAgain():
    while True:
        print_pause("do you wanna play again?")
        response = input("yes or no?")
        if (response == "yes"):
            print_pause("Restarting please wait...")
            startGame()
            break
        elif (response == "no"):
            print_pause("Thank you for playing.")
            break
        else:
            print_pause("wrong choice, please select from options only")
startGame()
