# from cars import *
import inspect
import time
from collections import Counter
import os



new_game = ""
class Game():
    def __init__(self, iterations = 0, acceptable_answers = ["Y", "YES", "NO", "N"]):
        self.iterations = iterations 
        self.acceptable_answers = acceptable_answers
    
    
    def race(self,contestants):
        heat_information = {}
        for car in contestants:
            i = 0
            print(f"**********")
            print(f"{car.name}")
            while self.iterations > i:
                car.movement()
                i += 1
                print(f"{car.name} has driven {car.position} units")
                time.sleep(.7)
                os.system('clear')
            print(f"{car.name} went {car.position} units")
            
            heat_information[car.name] = car.position
            time.sleep(.7)
            os.system('clear')
        self.winner(heat_information)
    
    def winner(self, heat):
        heat_dict = heat
        heat_counter = Counter(heat_dict)
        grab_winner = heat_counter.most_common(1)
        name, position = grab_winner[0]
        print(f"{name} won the race!!. They eneded up going {position} units!!!")


