class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know what to say")

class Cat(Animal):
    def speak(self):
        print("Meow")
class Dog(Animal):
    def speak(self):
        print("Bark")

class Fish(Animal):
    pass

A =Animal("Tim",19)
A.show()
c=Cat("Bill",34)
c.show()
c.speak()
f=Fish("Bubbles",19)
f.speak()