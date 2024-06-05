class Dog:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def bark(self):
        print(f"{self.name} is barking")
        
    

d1 = Dog("jessi", 11)
d1.eat()
d1.bark()
d2 = Dog("petty", 11)
d2.eat()
d2.bark()