import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_move = input("Enter : [r] for Rock, [p] for Paper or [s] for scissors:    ")
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

print()
print(f"You chose {player_move}")
print()

computer_number = random.randint(1,3)
computer_move = ''
if computer_number == 1:
    computer_move = rock
elif computer_number == 2:
    computer_move = paper
elif computer_number ==3:
    computer_move = scissors

print(f"The computer chose {computer_move}")
print()

if player_move == rock and computer_move == scissors or player_move == paper and computer_move == rock or player_move == scissors and computer_move == paper:
    print("You win!!")
elif player_move == rock and computer_move == paper or player_move == paper and computer_move == scissors or player_move == scissors and computer_move == rock:
    print("You lost...")
elif player_move == rock and computer_move == rock or player_move == paper and computer_move == paper or player_move == scissors and computer_move == scissors:
    print("Its a Draw?")
