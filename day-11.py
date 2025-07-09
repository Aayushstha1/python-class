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
    
    def __str__(self):
       return self.name
    
a=hello("Aayush",21)
a.name="Ram"
print(a.disc())

# a= hello ("Aayush" ,16)
# print(a)

# Aayush=hello("Aayush",16)
# Aayush.disc()

# class hi:
#  def __init__(self, Name, Address, phone):
#   self.Name= Name
#   self.Address= Address
#   self.phone= phone
#  def disc(self):
#          print(f" My Name is {self.Name} I live in {self.Address} and my phone no is {self.phone}")
#  def __str__(self):
#     Aayush=hi("Aayush", "damak",98000000)
# print(hi)






