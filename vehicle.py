class Vehicle:
    def __init__(self,make,model,colour):
        self.make = make
        self.model = model 
        self.colour = colour
    def move(self):
        print("starts moving")
    def hoot(self):
        print("honk honk")
class Bus(Vehicle):
    def __init__(self,make,model,colour,capacity):
        super().__init__(make,model,colour)
        self.capacity = capacity
    def start_boarding(self):
            print("The bus is now boarded")

class Lorry(Vehicle):
    def __init__(self,make,model,colour,maxload):
        super().__init__(make,model,colour)
        self.maxload = maxload
        
    def load(self):
        print("started loading")


