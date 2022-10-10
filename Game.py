import random, dice
import Warrior
import Soldier

w=Warrior.Warrior()
w.show()
s=Soldier.Soldier()
s.show()
v = random.randrange(1,7)

if v==1 or v==2 or v==3:
    w.strength =w.strength -2
    w.health =w.health -2
    w.logic = w.logic -2
    w.show()

elif v ==4 or v==5 or v==6:
    w.strength =w.strength +2
    w.health =w.health +2
    w.logic =w.logic +2
    w.show()
#setup
n=0
any = dice.apple()
yes_no = ["yes", "no", "y", "n"]
directions = ["left", "right", "forward", "backward"]

#Start of the game
name = input("What is your name? ") #user inputs their name
print("Welcome, " + name + ". Let's solve this hunting game!")
roll = input("Which role would you like to choose? role 1 or role 2. " ) #user gets to choose between the two roles
if roll == "role 1":
    print("role 1 = Warrior. you chose a Warrior.") #if user chooses role 1 then it's warrior.
elif roll == "role 2":
    print("role 2 = Soldier. you chose a Soldier.") #if user chooses role 2 then it's soldier.

player1_score = 0 # player 1 is user
player2_score = 0 # player 2 is monster

response = ""
points = 0
while response not in yes_no:
    response = input("Do you want to roll the dice? \nyes/no/y/n\n") #it asks user if they want to role the dice or not
    if response == "yes" or response == "y":
        no = random.randint(1,6) #dice range from 1 to 6
        any.dice(no) #shows the dice on terminal
        print("You rolled a:", no)
        print ("So you get ", no , " tries to win the game.\n") #shows user how many tries they have to win challenge 1
    elif response == "no" or response == "n":
        print("You are not ready for this game. Goodbye, " + name + ".") #if user says no then it quits the game
        quit()
    else: 
        print("I didn't understand that.\n")
        break

#part 1 of the game
for i in range(no):
    user = input("Enter a choice (rock, paper, scissors): ") #plays the rock, paper and scissors game.
    possible = ["rock", "paper", "scissors"]
    monster = random.choice(possible) #random input from the computer
    print(f"\nYou chose {user}, monster chose {monster}.\n")

    if user == monster:
        print("Both players selected {user}. It's a tie!") #if its a tie then no change in the points
        w.health == 0
    elif user == "rock":
        if monster == "scissors":
            print("Rock smashes scissors! You win!")
            player1_score = player1_score + 1  #This is how we increment a variablein points.
        else:
            print("Paper covers rock! You lose.")
            player2_score = player2_score + 1 #This is how we increment a variable in points.
            w.health == -1

    elif user == "paper":
        if monster == "rock":
            print("Paper covers rock! You win!")
            player1_score = player1_score + 1  #This is how we increment a variable in points.
        else:
            print("Scissors cuts paper! You lose.")
            player2_score = player2_score + 1 #This is how we increment a variable in points.
            w.health == -1
    elif user == "scissors":
        if monster == "paper":
            print("Scissors cuts paper! You win!")
            player1_score = player1_score + 1  #This is how we increment a variable in points.
        else:
            print("Rock smashes scissors! You lose.")
            player2_score = player2_score + 1 #This is how we increment a variable in points.
            w.health == -1
            
        points = points + no
print("Player 1 score:", player1_score) #prints the score for both players which is the user score and the monster(computer) score.
print("Player 2 score:", player2_score)

#part 2 of the game
class challeg2:
    def show(self):
        response = ""
        while response not in directions: #dice decides which direction the user will go
            print("To your left, you see a dead end.")
            print("To your right, there is a scary, dark forest.")
            print("There is a maze infront of you.")
            name3 = input("Would you like to roll the dice? ")
            if name3 == "yes" or name3 == "y":
                print("You rolled a: ", no)
                any.dice(no)
                if no == 1 or no == 2:
                    print("You chose the left direction. The road ends here. Farewell.")
                    quit()
                elif no == 3 or no == 4:
                    print("You chose the right direction.")
                    break
                elif no == 5 or no == 6:
                    print("You chose to move forward.")
                    break
                else:
                    print("I did not understand that. Try again!")
            elif name3 == "no" or name3 == "n":
                print("You are not ready for this game. Goodbye, " + name + ".")
                quit()
        print("write my story")

a = challeg2()
if player1_score < player2_score:
    print ("you lost! Goodbye, " + name + ".") #if user loses then the game ends
    exit()
if player2_score < player1_score:
    print ("you win! Congrats , " + name + ".") #congrats the user for winning
    name1 = input("do you want to continue playing? ") #asks user if they want to continue playing
    if response == "yes" or response == "y":
        print("Here is your next challenge: ")
        a.show()
    elif response == "no" or response == "n":
        print("You are not ready for this game. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
if player2_score == player1_score:
    name2 = input("do you want to continue playing? ")
    if response == "yes" or response == "y":
        print("Here is your next challenge: ")
        a.show()
    elif response == "no" or response == "n":
        print("You are not ready for this game. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")

#part 3 of the game
