# from cars import *
import inspect
import time



class Game():
    def __init__(self, iterations = 0, acceptable_answers = ["Y", "YES", "NO", "N"]):
        self.iterations = iterations 
        self.acceptable_answers = acceptable_answers
    
    
    def race(self,contestants):
        for car in contestants:
            i = 0
            print(f"**********")
            print(f"{car.name}")
            while self.iterations > i:
                car.movement()
                i += 1
                print(f"{car.name} has moved {car.position}spaces. It is going {car.speed} upt and accerating at {car.acceration} uptsquared. It has {car.nitro} units of nitro left")
                time.sleep(0.7)
            print(f"{car.name} went {car.position}")

    def start_game(self):
        get_user_input = ""
        while get_user_input not in self.acceptable_answers:
            try:
                if get_user_input in self.acceptable_answers:
                    break
                elif get_user_input not in self.acceptable_answers:
                    raise Exception ("Please only enter 'Y' or 'N' ")  
            except Exception:
                get_user_input = input("Would you like to play a game?\n Y / N\n").upper()




# new_game = Game(5)
# new_game.start_game()
# new_game.race([hero, player2, player3,player4])

# def isprop(v):
#     return isinstance(v, property)

# propnames = [name for (name, value) in inspect.getmembers(hero, isprop)]

# print(propnames)

