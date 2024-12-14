# 8.	Using hybrid inheritance ,create super class animal and respective derived class.

# Superclass (Base Class)
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Derived class 1: Mammal (Single Inheritance)
class Mammal(Animal):
    def __init__(self, name, legs):
        super().__init__(name)  # Calling the constructor of Animal
        self.legs = legs

    def walk(self):
        print(f"{self.name} walks on {self.legs} legs.")

# Derived class 2: Bird (Single Inheritance)
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)  # Calling the constructor of Animal
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} can fly with a wingspan of {self.wingspan} meters.")

# Derived class 3: Bat (Hybrid Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name, legs, wingspan):
        Mammal.__init__(self, name, legs)  # Calling the constructor of Mammal
        Bird.__init__(self, name, wingspan)  # Calling the constructor of Bird

    def display(self):
        print(f"{self.name} is a Bat with {self.legs} legs and a wingspan of {self.wingspan} meters.")
        
# Main code
bat = Bat("Batty", 2, 1.5)
bat.display()
bat.walk()  # Inherited from Mammal
bat.fly()  # Inherited from Bird
bat.sound()  # Inherited from Animal
