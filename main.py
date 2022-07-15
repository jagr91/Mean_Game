from random import randint
from time import sleep


def mean_game():
    print("Hello! You're about to play a very important game that can "
          "decide about a future of the entire Universe!")
    number = int(
        input("\nYou need to choose and write a number between 1 and 999\n>>>"))
    if number > 999:
        print('Number should be in between 1 and 999. Try again')
    else:
        print(f'You choose {number}. Excellent...')
        loading_sim()
        print(f'I am choosing {number + 1}')
        print('I WON!!!')


def loading_sim():
    for _ in range(randint(1, 5)):
        sleep(1)
        print('...')


if __name__ == '__main__':
    mean_game()
