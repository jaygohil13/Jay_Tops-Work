# Cricket Game :
 
print(""" ~~~~~~~~~~ Game of Cricket ~~~~~~~~~~
 
Introduction :
 
1. You have to select any random number from 1 to 6.
2. The computer will also select a number.
3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
   If the number selected by you and computer is same, then you will lose your wicket.
4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
   If the number selected by you and computer is same, then the computer will lose its wicket.
5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.
6. The innings will end after either the three wickets fell or the overs end.
7. The player with maximum runs wins. """)
 
print("\n---------- Start Game ----------")

import random

# Select the team :

l1 = ["CHENNAI SUPER KINGS", "KOLKATA KNIGHT RIDERS"]
computer = random.choice(l1)
user = input("Enter your team : ").upper()
print("Computer : ",computer)
print("User : ",user)

# Toss :

print("\nHere comes for the Toss")
toss = input("Choose Heads or Tails : ").lower()

random_toss = random.randint(1,2)          # In random_toss (1 = Heads) and (2 = Tails)
random_opt = random.randint(1,2)           # In random_opt (1 = bat) and (2 = ball)

u_opt = 0
c_opt = 0

if random_toss == 1 and toss == "Heads" :
    print("\nYou won the toss")
    u_opt = input("Choose bat or ball : ").lower()
elif random_toss == 2 and toss =="Tails":
    print("\nYou won the toss")
    u_opt = input("Choose bat or ball : ").lower()

else:
    print("\nYou lost the toss")

    if random_opt == 1:
        c_opt = "ball"
        print("Computer choose to",c_opt)

    elif random_opt == 2:
        c_opt = "ball"
        print("Computer choose to",c_opt)

# First Innings :

print("\n========== First Innings Begins ===========")

runs_1 = 0
wickets_1 = 0
balls_1 = 0

while wickets_1 != 2 and balls_1 != 12:
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
     
    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")
