import random


choices = ('r', 'p', 's')
emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}


def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or Scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice")


def display_choices(user_choice, computer_choices):
    print(f"You chose {emojis[user_choice]}")
    print(f"The computer chose {emojis[computer_choices]}")


def determine_winner(user_choice, computer_choices):
    if user_choice == computer_choices:
        print("Tie!!")

    elif (
            user_choice == 'r' and computer_choices == 's' or
            user_choice == 'p' and computer_choices == 'r' or
            user_choice == 's' and computer_choices == 'p'):

        print("You Win!")

    else:
        print("You lost :/ )")


def play_game():
    while True:

        user_choice = get_user_choice()
        computer_choices = random.choice(choices)

        display_choices(user_choice, computer_choices)
        determine_winner(user_choice, computer_choices)

        should_continue = input("Continue? (y/n): ")
        if should_continue == 'n':
            break


play_game()
