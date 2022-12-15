print("Welcome To Quiz Compitition")
username = input("username : ")

points = 0
playing = True
while playing == True:
   

    print(" 1.What is jersey number of virat kohli ?")
    Answer_1 = input("Fill in here : ")
    if Answer_1 == "18" or Answer_1 == "18":
       points += 10
       print("Correct !")
       
    else:
        points -= 20
        print("Wrong !")
        

    print("2.What is the capital of india ?")
    Answer_2 = input("Fill in here : ")
    if Answer_2 == "New Delhi" or Answer_2 == "new delhi":
        print("Correct !")
        points +=10
    else:
        print("Wrong !")
        points -= 20

    print("3.Who is india's prime minister ?")
    Answer_3 = input("Fill in here : ")
    if Answer_3 == "Narendra Modi" or Answer_3 =="narendra modi":
        print("Correct !")
        points += 10
    else:
        print("Wrong !")
        points -= 20

    print("points :",points)
    
    choice = input("do you want to play again ? : ")
    if choice == 'n' or choice == "no":

        playing = False
   
    