class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am a dog my name is {self.name} and im {self.age} years old ")
    def make_sound(self):
        print("I bark")
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Im a cat mya name is {self.name} Im {self.age} years old")
    def make_sound(self):
        print("I meow")
obj1=dog("milu",2)
obj2=cat("thomas",3)

for domestic in (obj1,obj2):
    domestic.info()
    domestic.make_sound()
    
        