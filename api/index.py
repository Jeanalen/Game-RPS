import random 

choices = ["rock", "paper", "scissors"] 

def determine_winner(player_choice, computer_choice): 
    if player_choice == computer_choice: 
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"): 
        return "win"
    else: #If none of the winning conditions are met, it defaults to returning "lose".
        return "lose"

def play_game(): 
    print("Welcome to Rock, Paper, Scissors!") 
    print("Type 'quit' to exit the game.") 
    print("Choices: rock, paper, scissors") 
    print("-" * 30)  

    total_wins = 0
    total_losses = 0
    total_ties = 0 #Initializes counters for total wins, losses, and ties.
    attempts = 0
    max_attempts = 10 #Sets the attempt counter to zero and defines the maximum number of attempts allowed (10).

    while attempts < max_attempts: #Starts a loop that will continue until the number of attempts reaches the maximum limit.
        player_choice = input("Your choice (human): ").lower() #Prompts the player to enter their choice and converts it to lowercase for consistency.
        
        if player_choice == 'quit': #If the player types 'quit', it prints a goodbye message and exits the loop.
            print("Thanks for playing! Goodbye!")
            break
        
        if player_choice not in choices: 
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices) #Randomly selects a choice for the computer from the choices list.
        print(f"\nComputer chose: {computer_choice}") #Displays the computer's choice to the player.
        
        result = determine_winner(player_choice, computer_choice) 

        if result == "win": #If the result is a win, it prints a win message and increments the total wins counter.
            print("\nYou win!")
            total_wins += 1
        elif result == "lose": #If the result is a loss, it prints a lose message and increments the total losses counter.
            print("\nYou lose!")
            total_losses += 1
        else: #If the result is a tie, it prints a tie message and increments the total ties counter.
            print("\nIt's a tie!")
            total_ties += 1
        
        attempts += 1 #Increments the attempts counter by 1.
        print(f"\nScores after {attempts} attempts: Wins: {total_wins}, Losses: {total_losses}, Ties: {total_ties}") #Displays the current scores after the player's choice.
        print("-" * 30)  # Divider line ; Prints a line of dashes to separate rounds visually.
    
    if attempts == max_attempts: #After exiting the loop, if the maximum attempts have been reached, it prints a message indicating that and displays the final score.
        print("\nMaximum attempts reached! Thanks for playing!")
        print(f"Final Score: Wins: {total_wins}, Losses: {total_losses}, Ties: {total_ties}")

        if total_wins > total_losses:
            print("\n🏆 Overall Winner: PLAYER (You)!")
        elif total_losses > total_wins:
            print("🤖 Overall Winner: COMPUTER!")
        else:
            print("\n🤝 Overall Result: IT'S A TIE!")

if __name__ == "__main__": 
    play_game()
