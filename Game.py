import random, dice
import Warrior
import Soldier

w=Warrior.Warrior()
s=Soldier.Soldier()
v = random.randint(1,6)
    
#setup
n=0
any = dice.apple()
yes_no = ["yes", "no", "y", "n"]
directions = ["left", "right", "forward"]

#Start of the game
name = input("What is your name? ") #user inputs their name
print("Welcome, " + name + ". Let's solve this hunting game!")
roll = input("Which role would you like to choose? role 1 or role 2. ") #user gets to choose between the two roles
if roll == "role 1":
    print("role 1 = Warrior. you chose a Warrior.") #if user chooses role 1 then it's warrior.
elif roll == "role 2":
    print("role 2 = Soldier. you chose a Soldier.") #if user chooses role 2 then it's soldier.

if roll == "role 1":
    v==1 or v==2 or v==3
    w1 =w.strength 
    w2 =w.health 
    w3 = w.logic 
    
elif v ==4 or v==5 or v==6:
    w1 =w.strength
    w2 =w.health 
    w3 =w.logic 

elif roll == "role 2" or v==1 or v==2 or v==3:
    s1 = s.strength 
    s2 = s.health 
    s3 = s.logic

elif v==4 or v==5 or v==6:
    s1 = s.strength
    s2 = s.health
    s3 = s.logic
     

print('''You live in a kingdom serving for the King. It looks like someone has stolen his crown.
The King suspects someone from the kingdom might has stolen it.
He appoints you to find it for him. He also promises you to reward you for doing him this favour.
Will you be able to find his crown?
Let's start playing the game. All the best!''')

player1_score = 0 # player 1 is user
player2_score = 0 # player 2 is monster

print("Here you are on the quest to find the crown. Your first challenge is to defeat the monster.")

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
        if roll == "role 1":
                print("w.strength = 0",w.strength)
        elif roll == "role 2":
                print("s.strength = 0",w.strength)
    elif user == "rock":
        if monster == "scissors":
            print("Rock smashes scissors! You win!")
            if roll == "role 1":
                print("w.strength = +1",w.strength)
            elif roll == "role 2":
                print("s.strength = +1",s.strength)
            player1_score = player1_score + 1  #This is how we increment a variablein points.
        else:
            print("Paper covers rock! You lose.")
            if roll == "role 1":
                print("w.strength = -1",w.strength)
            elif roll == "role 2":
                print("s.strength = -1",s.strength)
            player2_score = player2_score + 1 #This is how we increment a variable in points.
    elif user == "paper":
        if monster == "rock":
            print("Paper covers rock! You win!")
            if roll == "role 1":
                print("w.strength = +1",w.strength)
            elif roll == "role 2":
                print("s.strength = +1",s.strength)
            player1_score = player1_score + 1  #This is how we increment a variable in points.
        else:
            print("Scissors cuts paper! You lose.")
            if roll == "role 1":
                print("w.strength = -1",w.strength)
            elif roll == "role 2":
                print("s.strength = -1",s.strength)
            player2_score = player2_score + 1 #This is how we increment a variable in points.
    elif user == "scissors":
        if monster == "paper":
            print("Scissors cuts paper! You win!")
            if roll == "role 1":
                print("w.strength = +1",w.strength)
            elif roll == "role 2":
                print("s.strength = +1",s.strength)
            player1_score = player1_score + 1  #This is how we increment a variable in points.
        else:
            print("Rock smashes scissors! You lose.")
            if roll == "role 1":
                print("w.strength = -1",w.strength)
            elif roll == "role 2":
                print("s.strength = -1",s.strength)
            player2_score = player2_score + 1 #This is how we increment a variable in points.
            
        points = points + no
print("Player 1 score:", player1_score) #prints the score for both players which is the user score and the monster(computer) score.
print("Player 2 score:", player2_score)

#part 2 of the game
class challeg2:
    def show(self):
        response = ""
        while response not in directions: #dice decides which direction the user will go
            print('''you now reach to a three path way. now the dice decides which of the three paths you would choose.
To your left, you see a dead end.
To your right, there is a scary, dark forest.
If you move forward then you reach a treasure chest".
This looks more like a maze is infront of you.''')
            name3 = input("Would you like to roll the dice? ")
            if name3 == "yes" or name3 == "y":
                print("You rolled a: ", no)
                any.dice(no)
                if no == 1 or no == 2:
                    print("You chose the left direction. The road ends here. Farewell.")
                    if roll == "role 1":
                     print("w.health = -1",w.health)
                    elif roll == "role 2":
                     print("s.health = -1",s.health)
                    quit()
                elif no == 3 or no == 4:
                    print("You chose the right direction.You head deeper into the forest and get eaten by a bear.")
                    if roll == "role 1":
                     print("w.health = -2",w.health)
                    elif roll == "role 2":
                     print("s.health = -2",s.health)
                    break
                elif no == 5 or no == 6:
                    print("You chose to move forward.You win! You have now entered challenge 3.")
                    if roll == "role 1":
                     print("w.health = +2",w.health)
                    elif roll == "role 2":
                     print("s.health = +2",s.health)
                    name4 = input("do you want to roll the dice? ")
                    if name4 == "yes" or name4 == "y":
                      print("You rolled a: ", no)
                      any.dice(no)
                      if no == 1 or no == 2 or no == 3:
                            print("You got a ",no,". you find the crown and return it to the King! Congrats,"+name+" you won the game.")
                            if roll == "role 1":
                             print("w.logic = +2",w.logic)
                            elif roll == "role 2":
                             print("s.logic = +2",s.logic)
                            quit()
                      elif no == 4 or no == 5 or no == 6:
                           print("you got a",no,". You couldn't find the crown. You lost the game! Goodbye,"+name+"")
                           if roll == "role 1":
                            print("w.logic = -2",w.logic)
                           elif roll == "role 2":
                            print("s.logic = -2",s.logic)
                           quit()
                    else: name4 == "no" or name4 == "n"
                    print("Goodbye,"+name+"")
                else:
                    print("I did not understand that. Try again!")
            elif name3 == "no" or name3 == "n":
                    print("You are not ready for this game. Goodbye, " + name + ".")
                    quit()

a = challeg2()
if player1_score < player2_score: #if user score is less than the monster score then the game ends
    print ("you lost! Goodbye," + name + ".") #if user loses then the game ends
    exit()
if player2_score < player1_score: #if user score is greater than the monster score then the user wins
    print ("you win! Congrats," + name + ".") #sneds a congrats the user for winning
    name1 = input("do you want to continue playing? ") #asks user if they want to continue playing
    if response == "yes" or response == "y": #using if else statement for response from the user
        print("Here is your next challenge: ")
        a.show()
    elif response == "no" or response == "n": #if user does not want to play then the game ends when user types in "no"
        print("You are not ready for this game. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
if player2_score == player1_score:
    name2 = input("do you want to continue playing? ") #asks the user if they want to continue playing
    if response == "yes" or response == "y":
        print("Here is your next challenge: ")
        a.show()
    elif response == "no" or response == "n":
        print("You are not ready for this game. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
