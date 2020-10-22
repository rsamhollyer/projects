class Game():
    def __init__(self, iterations):
        self.iterations = iterations 
    
    def race(self,contestants):
        for car in contestants:
            i = 0
            
            while self.iterations <= i:
                car.race()    
                i += 1





