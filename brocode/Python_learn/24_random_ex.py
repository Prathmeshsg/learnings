# number guessing game
import random

# low_num = 1
# high_num = 100
# answer = random.randint(low_num, high_num)
# guesses = 0
# is_running = True

# print("Python number guessing game")

# print(f"Guess a number between {low_num} and {high_num}")

# while is_running: 
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < low_num or guess > high_num:
#             print(f"Out of range, Please guess a number between {low_num} and {high_num}")
#         elif guess < answer:
#             print("Too low! Try again")
#         elif guess > answer:
#             print("Too high! Try again")
#         else:
#             print(f"CORRECT! The answer is {answer}")
#             print(f"You got it in {guesses} guesses!")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please guess a number between {low_num} and {high_num}")
        
##################################################

# rock paper scissor game

# options = ("rock", "paper", "scissors")

# running = True

# while running:
#     player = None
#     computer_choice = random.choice(options)
#     while player not in options:
#         player = input("Enter your choice: ").lower()

#     print(f"Player: {player}")
#     print(f"Computer: {computer_choice}")

#     if player == computer_choice:
#         print("Draw")
#     elif player == "rock" and computer_choice == "scissors":
#         print("You wins")
#     elif player == "paper" and computer_choice == "rock":
#         print("You wins")
#     elif player == "scissors" and computer_choice == "paper":
#         print("You wins")
#     else:
#         print("Computer wins")
        
    
#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False
        
# print("Thanks for playing!")


###################################################

# dice roll program

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│    ●    │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│         │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│    ●    │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
    
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
##########
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()
    
for die in dice:
    total += die

print(f"Total: {total}")

