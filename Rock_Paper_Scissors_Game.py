import random

def get_user_choice():
    while True:
        print("\nChoose your move:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("4 - Quit game")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def print_choices(player_choice, computer_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    print(f"\nYou chose: {choices[player_choice - 1]}")
    print(f"Computer chose: {choices[computer_choice - 1]}")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'DRAW'
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        return 'PLAYER'
    else:
        return 'COMPUTER'

def display_result(result):
    if result == 'DRAW':
        print("It's a draw!")
    elif result == 'PLAYER':
        print("You win!")
    else:
        print("Computer wins!")

def rock_paper_scissors():
    player_score = 0
    computer_score = 0
    
    print('Welcome to Rock, Paper, Scissors!')

    while True:
        player_choice = get_user_choice()
        
        if player_choice == 4:
            break
        
        computer_choice = random.randint(1, 3)
        print_choices(player_choice, computer_choice)
        
        result = determine_winner(player_choice, computer_choice)
        display_result(result)
        
        if result == 'PLAYER':
            player_score += 1
        elif result == 'COMPUTER':
            computer_score += 1
        
        print(f"\nCurrent Score - You: {player_score} | Computer: {computer_score}")
    
    print("\nThanks for playing!")
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")

# Start the game
rock_paper_scissors()
