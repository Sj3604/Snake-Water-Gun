import random

# Define the choices
choices = {-1: "Snake", 0: "Water", 1: "Gun"}

# Initialize scores
user_score = 0
computer_score = 0
draws = 0

print("🎮 Welcome to Snake-Water-Gun Game!")
print("Instructions: Enter -1 for Snake, 0 for Water, 1 for Gun")

# Game loop
while True:
    # Get user input
    try:
        user_input = int(input("\nYour choice (-1 for Snake, 0 for Water, 1 for Gun): "))
        if user_input not in [-1, 0, 1]:
            print("❌ Invalid input. Please enter -1, 0, or 1.")
            # if we not use continue it would execute next statements even after getting the wrong input
            continue
    except ValueError:
        print("❌ Invalid input. Please enter an integer.")
        continue

    # Computer's random choice
    computer_input = random.choice([-1, 0, 1])

    # Display choices
    print(f"You chose: {choices[user_input]}")
    print(f"Computer chose: {choices[computer_input]}")

    # Determine the winner
    if user_input == computer_input:
        print("⚖️ It's a draw!")
        draws += 1
    elif (user_input == -1 and computer_input == 0) or \
         (user_input == 0 and computer_input == 1) or \
         (user_input == 1 and computer_input == -1):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    # Show score
    print(f"🔢 Score => You: {user_score} | Computer: {computer_score} | Draws: {draws}")

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

# Final score
print("\n🏁 Game Over!")
print(f"Final Score => You: {user_score} | Computer: {computer_score} | Draws: {draws}")
if user_score > computer_score:
    print("🎉 Congratulations! You won the game!")
elif computer_score > user_score:
    print("😢 You lost the game. Better luck next time!")
else:
    print("🤝 It's a tie!")

give a small description for the game 




