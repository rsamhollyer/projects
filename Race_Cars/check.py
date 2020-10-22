from cars import *

class Player(Cars):
    def movement(self):
        
        # if random.randint(1,10) == 10:
        #     print(f"{self.name} is driving perfectly! What a champ.")
        #     self.accerate()
        #     self.position += 2 * self.speed 
        #     if self.speed > self.top_speed:
        #         self.speed = self.top_speed
        # elif random.randint(1,10) > 1:
        #     self.accerate()
        #     self.decelerate()
        #     self.brake()
        #     self.position += self.speed 
        #     if self.speed > self.top_speed:
        #         self.speed = self.top_speed
        # else:
        #     print(f"Oh no! {self.name} has hit the wall!")
        #     self.speed = 0
        #     self.position += self.speed

hero = Player("Check",20,10,10)

hero.movement()