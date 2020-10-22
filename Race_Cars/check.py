import random

class Cars():
    def __init__(self, name, top_speed, acceration, max_acceleration, position = 0, speed = 0, wheels = 4, nitro = 2):
        self.name = name
        self.top_speed = top_speed
        self.acceration = acceration
        self.max_acceleration = max_acceleration
        self.position = position    
        self.speed = speed
        self.wheels = wheels
        self.nitro = nitro

    def accerate(self):
        self.acceration = self.max_acceleration
        self.speed += self.acceration
        if self.nitro > 0:
            if random.randint(1,6) > 1:
                self.speed += 2 * self.acceration
                self.nitro -= 1 

    def brake(self):
        if self.speed > 0:
            self.speed -= random.randint(0,3)

    def decelerate(self):
        if self.acceration > 0:
            self.acceration -= random.randint(0,2)

    def movement(self):
        if random.randint(1,10) == 10:
            print(f"{self.name} is driving perfectly! What a champ.")
            self.accerate()
            self.position += 2 * self.speed 
            if self.speed > self.top_speed:
                self.speed = self.top_speed
        elif random.randint(1,10) > 1:
            self.accerate()
            self.decelerate()
            self.brake()
            self.position += self.speed 
            if self.speed > self.top_speed:
                self.speed = self.top_speed
        else:
            print(f"Oh no! {self.name} has hit the wall!")
            self.speed = 0
            self.position += self.speed

class Player(Cars):
    def __init__(self, name, top_speed, acceration, max_acceleration, position = 0, speed = 0, wheels = 4, nitro = 2):
        super().__init__( name, top_speed, acceration, max_acceleration, position = 0, speed = 0, wheels = 4, nitro = 2)
    
    def movement(self):
        get_player_input = 0
        while get_player_input not in range(1,2):
            
            try:
                get_player_input = int(input("""It's your time to shine, champ. What do you want to do?

1. I want to push it to the limit. (WARNING. Great reward but high risk!!!)
2. I want to drive normally 
>

"""))
                
                if get_player_input in range(1,2):
                    break
                elif get_player_input not in range(1,2):
                    raise ValueError
            except ValueError:
                print("Please enter 1, 2 ,3 ")


        if get_player_input == 1:
            if random.randint(1,5) > 3:
                print(f"{self.name} is driving perfectly! What a champ.")
                self.accerate()
                self.position += 2.5 * self.speed 
                
                if self.speed > self.top_speed:
                    self.speed = self.top_speed
            
            else:
                print(f"Oh no! {self.name} has hit the wall!")
                self.speed = 0
                self.position += self.speed        

        elif get_player_input == 2:
            
            if random.randint(1,10) > 1:
                self.accerate()
                self.decelerate()
                self.brake()
                self.position += self.speed 
                
                if self.speed > self.top_speed:
                    self.speed = self.top_speed
            
            else:
                print(f"Oh no! {self.name} has hit the wall!")
                self.speed = 0
                self.position += self.speed


hero = Player("Thunder", 20, 5,5)
player2 = Cars("Blaze",17, 8,8)
player3 = Cars("Inferno", 30, 3,3)
player4 = Cars("Blizzard", 10, 4,4)

all_cars = [hero,player2, player3,player4]

hero.movement()