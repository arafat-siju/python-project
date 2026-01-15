import random

user_dict = {"s": 1, "w": 2, "g": 3}
reverse_dict = {1: "Snake🐍", 2: "Water💧", 3: "Gun🔫"}

winning_rules = {
    1: 2,  # Snake drinks Water
    2: 3,  # Water disables Gun
    3: 1   # Gun kills Snake
}

user_score = 0
computer_score = 0

while True:
    print("\n================== Snake-Water-Gun Game ==================")
    print("Rule: Enter s for Snake, w for Water, g for Gun\nEnter q to Quit the game.")

    computer = random.choice([1, 2, 3])
    user_str = input("\nEnter your choice: ").lower()

    if user_str == "q":
        print(f"\nThanks for playing! Final Score → You: {user_score} | Computer: {computer_score}\n")
        break

    if user_str not in user_dict:
        print("\n❌ Invalid Choice! Try again.")
        continue

    user = user_dict[user_str]

    print(f"\nComputer chose: {reverse_dict[computer]}\nYou chose: {reverse_dict[user]}\n")

    if(computer == user):
        print("🤝 It's a Draw!")
    elif(winning_rules[user] == computer):
        print("🎉 HURRAH! You Win.")
        user_score += 1
    else:
        print("💻 Computer Wins. You Lose.")
        computer_score += 1

    print(f"\n📊 Score → You: {user_score} | Computer: {computer_score}")
    print("\n---------- Thank You ----------\n")