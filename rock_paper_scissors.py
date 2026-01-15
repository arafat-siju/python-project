'''
rock: 1
paper: 2
scissor: 3
'''

import random

user_dict = {"r": 1, "p": 2, "s": 3}
reverse_dict = {1 : "Rock👊", 2 : "Paper🖐️", 3 : "Scissor✌️"}

user_score = 0
computer_score = 0

while True:
    print("================== Rock-Paper-Scissors Game ==================")
    print("Rule: Enter r for Rock, p for Paper, s for Scissor\nEnter q for Quit the game.")

    computer = random.choice([1, 2, 3])
    user_str = input("\nEnter your choice: ").lower()
    
    if(user_str == "q"):
        print("Thanks for playing.")
        break
    if(user_str not in user_dict):
        print("\nInvalid Choice! Try again.")
        print("     -------x-------      \n")
        continue
    
    user = user_dict[user_str]

    print(f"\nComputer choose: {reverse_dict[computer]}\nYou choose: {reverse_dict[user]}\n")
    
    if(computer == user):
        print("It is Draw!")
    else:
        if(computer == 1 and user == 2):
            print("🎉HURRAH! You Win.")
            user_score += 1
        elif(computer == 1 and user == 3):
            print("You Lose.")
            computer_score += 1
        elif(computer == 2 and user == 1):
            print("You Lose.")
            computer_score += 1
        elif(computer == 2 and user == 3):
            print("🎉HURRAH! You Win.")
            user_score += 1
        elif(computer == 3 and user == 1):
            print("🎉HURRAH! You Win.")
            user_score += 1
        elif(computer == 3 and user == 2):
            print("You Lose.")
            computer_score += 1
        else:
            print("Something went wrong!")

    print(f"\n📊Score → You: {user_score} | Computer: {computer_score}")
    print("\n---------- Thank You ----------\n")