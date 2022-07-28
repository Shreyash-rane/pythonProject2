# Stone paper scissor game
def SPS():
    import random
    choices = ['Stone','Paper','Scissors']
    store_choice = random.choice(choices)
    user_choice = input("Enter your choice: ")

    if (user_choice == 'Stone' and store_choice == 'Stone' ):
        print("its a tie")
    elif (user_choice == 'Stone' and store_choice == 'Paper' ):
        print("You lose")
    elif (user_choice == 'Stone' and store_choice == 'Scissors' ):
        print("You won")
    if (user_choice == 'Paper' and store_choice == 'Stone' ):
        print("its a Win")
    elif (user_choice == 'Paper' and store_choice == 'Paper' ):
        print("ITs a Tie")
    elif (user_choice == 'Paper' and store_choice == 'Scissors' ):
        print("You lose")
    if (user_choice == 'Scissors' and store_choice == 'Stone' ):
        print("You Lose")
    elif (user_choice == 'Scissors' and store_choice == 'Paper' ):
        print("You Win")
    elif (user_choice == 'Scissors' and store_choice == 'Scissors' ):
        print("Its a TIe")


looper = 1
while(looper == 1):
    SPS()
    looper = int(input("Do you want to play again? Press 1 to play again: "))        

    