import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]


print("Welcome to the Rock, Paper and Scissors")

while True:

    while True:
        try:
            user_choice = int(input("What do you choose? Type 0 for Rock, "
                                "1 for Paper and 2 for Scissors "))
            if user_choice < 0 or user_choice > 2:
                print("You must write 0, 1 or 2")
                continue
        
            print("You chose: ")
            print(game_images[user_choice])

            break
        except (ValueError, IndexError):
            print("You must write 0, 1 or 2")

    computer_choice = random.randint(0, 2)
    print("Computer chose:  ")
    print(game_images[computer_choice])


    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. You lose! ")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! ")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose! ")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win! ")
    elif computer_choice == user_choice:
        print("It's a draw! ")

    play_again = input("Do you want to play again? Type 'y' for yes, or any other key to quit: ").lower()

    if play_again != 'y':
        print("Thanks for playing! Goodbye. ")
        break

