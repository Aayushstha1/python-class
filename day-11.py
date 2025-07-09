# class hello:
    # name = "Aayush"
    # h = hello()  
# print(h.name)
class hello:
    def __init__(self,name, age):
        self.name=name
        self.age=age
        
        
    def disc(self):
            print(f"My name is {self.name} and age is {self.age}")

Aayush=hello("Aayush",16)
Aayush.disc()


