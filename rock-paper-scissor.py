import random

# Declaring constants for choices
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

# Emojis for visual representation
emojis = { ROCK: '⛰️', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

# Ask the user to make a valid choice (user input)
def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

# Show what both players chose
def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

# Determine outcome of a single round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == SCISSORS and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print('You win')
    else:
        print('You lose')

# Play multiple rounds (optional)
def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    total_wins = 0
    total_losses = 0
    total_ties = 0

    while True:
        user_score = 0
        computer_score = 0
        round_num = 1

        print("\n🎮 Starting a best of 3 match...")

        # Loop until either the player or computer wins 2 rounds
        while user_score < 2 and computer_score < 2:
            print(f"\n--- Round {round_num} ---")
            round_num += 1

            user_choice = get_user_choice()
            computer_choice = random.choice(choices)

            display_choices(user_choice, computer_choice)

            if user_choice == computer_choice:
                print("It's a tie!")
                total_ties += 1  # Count round ties
            elif (
                (user_choice == ROCK and computer_choice == SCISSORS) or
                (user_choice == SCISSORS and computer_choice == PAPER) or
                (user_choice == PAPER and computer_choice == ROCK)
            ):
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

        # Announce match winner
        print("\n🏁 Match over!")
        if user_score == 2:
            print("🏆 You win the match!")
            total_wins += 1  # Track match win
        else:
            print("🏆 Computer wins the match!")
            total_losses += 1  # Track match loss

        # Ask if user wants another match
        while True:
            should_continue = input("\nPlay another match? (y/n): ").lower()
            if should_continue == 'y':
                break # Continue the outer loop
            elif should_continue == 'n':
                # Print stats after all matches
                print("\n📊 Final Stats:")
                print(f"Wins: {total_wins}")
                print(f"Losses: {total_losses}")
                print(f"Ties: {total_ties}")
                return
            else:
                print("Invalid input! Please enter 'y' to continue or 'n' to quit.")

play_game()
