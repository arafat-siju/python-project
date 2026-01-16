import random

def play_game():
    print("\n============= Welcome to the Number Guessing Game! =============")
    print("\nRobot: I am thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!\n")
    
    robot_guess_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while (attempts < max_attempts):
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if (guess < 1 or guess > 100):
                print("Please guess a number between 1 and 100!")
                attempts -= 1
                continue
            
            if (guess < robot_guess_number):
                print("📈 Too low! Try a higher number.\n")
            elif (guess > robot_guess_number):
                print("📉 Too high! Try a lower number.\n")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {robot_guess_number}!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            attempts -= 1
    else:
        print(f"\n😔 Game Over! You've used all {max_attempts} attempts.")
        print(f"The number was {robot_guess_number}. Better luck next time!")
    
    print("\n==============  ===============")

def main():
    while True:
        play_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break
        print("\n")

if __name__ == "__main__":
    main()