# class animal:
#     def __init__(self,name):
#          self.name=name
         
         
# class person (animal):
#     def __init__(self,age, name):
#         super().__init__(name)
#         self.age=age
        
# p=person("Aayush",21)
# print(p.age)
# print(p.name)

class father:
    def __init__(self,name):
        self.name=name
        
class mother:
    def __init__(self,age):
        self.age=age
    
class son(father,mother):
    def __init__(self, name, age, Address):
        father.__init__(self, name)
        mother.__init__(self, age)
        self.Address = Address
s=son ("Aayush", 22,"Ktm")
print(s.age)
print(s.name)
print(s.Address)
print(f"My name is {s.name}, I am {s.age} years old and I live in {s.Address}")
