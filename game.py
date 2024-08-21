# game.py

from utils import print_intro
from scenes import scene_one

def start_game():
    print_intro()
    scene_one()

if __name__ == "__main__":
    while True:
        start_game()
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again != "y":
            break
