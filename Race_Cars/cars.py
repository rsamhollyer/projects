class Cars():
    def __init__(self, name, top_speed, acceration, position = 0, speed = 0, wheels = 4, nitro = 2):
        self.name = name
        self.top_speed = top_speed
        self.acceration = acceration
        self.position = position    
        self.speed = speed
        self.wheels = wheels
        self.nitro = nitro

    def accerate(self):
        if self.nitro > 0:
            self.speed += 2 * self.acceration
            self.nitro -= 1 
        else:
            self.speed += self.acceration

    def brake(self):
        if self.speed > 0:
            self.speed -= 1

    def decelerate(self):
        if self.acceration >0:
            self.acceration -= 1

    def movement(self):
        self.accerate()
        self.decelerate()
        self.brake()
        self.position += self.speed 
        if self.speed > self.top_speed:
            self.speed = self.top_speed


class Player(Cars):
    pass

hero = Player("Thunder", 20, 5)
player2 = Cars("Blaze",17, 8)
player3 = Cars("Thunder", 30, 3)
player4 = Cars("Thunder", 10, 4)
