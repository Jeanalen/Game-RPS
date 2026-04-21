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

@app.route('/api/play', methods=['POST'])
def play():
    # Get the player choice from the website
    data = request.get_json()
    player_choice = data.get('choice', '').lower()

    if player_choice not in choices:
        return jsonify({"error": "Invalid choice"}), 400

    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)

    # Return the result as JSON instead of printing it
    return jsonify({
        "player": player_choice,
        "computer": computer_choice,
        "result": result
    })

# Necessary for Vercel entrypoint
if __name__ == "__main__":
    app.run()
