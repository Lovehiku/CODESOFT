import random

# Instructions
print("Welcome to Rock, Paper, Scissors!")
print("Instructions: Choose 'rock', 'paper', or 'scissors'.")
print("The computer will also choose one, and the winner will be determined based on these rules:")
print(" - Rock beats Scissors")
print(" - Scissors beats Paper")
print(" - Paper beats Rock\n")

# Initialize scores
user_score = 0
computer_score = 0

# Game loop
while True:
    # Ensure the user inputs a valid choice
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    
    # Validate user input
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()

    # Computer's random choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "You win! Rock beats scissors."
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You win! Scissors beats paper."
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        result = "You win! Paper beats rock."
        user_score += 1
    else:
        result = f"You lose! {computer_choice.capitalize()} beats {user_choice}."
        computer_score += 1

    # Show result and scores
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print(result)
    print(f"Score: You - {user_score}, Computer - {computer_score}")

    # Play again?
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break  # Exit the loop and end the game
