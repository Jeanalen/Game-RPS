from flask import Flask, request, jsonify
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

@app.route('/')
def play():
    # Get the player's choice from the URL (e.g., ?choice=rock)
    player_choice = request.args.get('choice', '').lower()
    
    if not player_choice:
        return "<h1>Welcome!</h1><p>Add <b>?choice=rock</b> to the end of your URL to play!</p>"

    if player_choice not in choices:
        return jsonify({"error": "Invalid choice. Pick rock, paper, or scissors."})

    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)

    return jsonify({
        "player": player_choice,
        "computer": computer_choice,
        "result": result,
        "message": f"You {result}!"
    })
