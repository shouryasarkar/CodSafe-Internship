import random 

# User Choice
def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock,paper, or scissors): ").lower()
        if user_input in ["rock","paper","scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter rock, paper, or scissors")

    # choices = ['rock', 'paper', 'scissors']
    # return random.choice(choices)
       
# Computer Choice
def get_computer_choice():
    choice = random.choice(["rock", "paper", "scissors"])
    return choice

# Main Function
def choose_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "User"
    else:
        return "Computer"

# View result
def view_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "Tie":
        print("The game is a tie.")
    elif winner == "User":
        print("YOU WIN")
    else:
        print("YOU LOOSE")

# Play Game
def play_game():
    user_score = 0
    computer_score = 0
    play_again = "yes"

    while play_again.lower() == "yes":
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = choose_winner(user_choice,computer_choice)

        if winner == "User":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1

        view_result(user_choice,computer_choice,winner)

        print(f"\nScore: You {user_score} - {computer_score} Computer")
        play_again = input("\nDo You Want to Play Again? (Yes/No): ")
    
    print("\nThanks for playing! Final Score:")
    print(f"You: {user_score} - Computer: {computer_score}")

# Run the game 
play_game()