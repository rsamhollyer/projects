from game import *
from cars import *



new_game = Game(5)
def start_game():#This runs the game. It is called in the Start_game script and when a 'Y' is entered it runs the race() method which starts the game for the player
    global get_user_input
    get_user_input = ""
    while True:
        try:
            if get_user_input == "YES" or get_user_input == "Y":
                new_game.race(all_cars)
                break
            elif get_user_input not in new_game.acceptable_answers:
                raise Exception ("Please only enter 'Y' or 'N' ")
            else:
                break
        except Exception:
            get_user_input = input("Would you like to play a game?\n Y / N\n").upper()
