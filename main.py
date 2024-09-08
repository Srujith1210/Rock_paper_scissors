
import random

options = ("rocks","paper","scissors")
running = True



while running:

  player = None
  computer = random.choice(options)
  
  
  while player not in options:
    player = input("Enter a choice (rock, paper, scissors):")
    
    
    print(f"Player:{player}")
    print(f"computer:{computer}")
    if player == computer:
      print("Its a tie!")
    elif player == "rock" and computer == "scissors":
      print("You win!")
    elif player == "paper" and computer == "rock":
     print("You win!")
    elif player ==  "scissors" and computer == "paper":
     print("You win!")
    else:
     print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
      running = False

print("Thanks for playing!")
         

