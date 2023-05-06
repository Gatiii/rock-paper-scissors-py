import random

user = input("type your choice: ")
actions = ["rock", "paper", "scissors"]
computer_action = random.choice(actions)

if computer_action == user:
    print(f"tie you both selected {user}")
if computer_action == "rock" and user == "scissors":
    print(f"{computer_action} computer wins")
if computer_action == "paper" and user == "scissors":
    print(f"{computer_action} you win")
if computer_action == "rock" and user == "paper":
    print(f"{computer_action} you win")
if computer_action == "scissors" and user == "paper":
    print(f"{computer_action} computer wins")
if computer_action == "paper" and user == "rock":
    print(f"{computer_action} computer wins")
if computer_action == "scissors" and user == "rock":
    print(f"{computer_action} you win")