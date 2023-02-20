'''1. Create a class named 'Dog'. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

🔴 a. It should have a function 'description()' which prints the name and age of the dog.
🔴 b. It should have a function 'get_info()' which prints the coat color of the dog.
🔴 c. Create child classes 'JackRussellTerrier' and 'Bulldog' which is inherited from the class 'Dog'. It should have at least two methods of its own.
🔴 d. Create objects and implement the above functionalities. 
'''

# Hierarchical Inheritance


class Dog:                                                     # Parent class
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Parent class property:")
        print(f"Dog name: {self.name}\nAge: {self.age}\n")

    def get_info(self):
        print("Coat color of dog: ",self.coat_color,"\n")

class JackRussellTerrier(Dog):                                 # Child Class inheriting parent class
    def dogcolor(self,dog_color):
        self.dog_color = dog_color
        print("Properties of JackRussellTerrier:")
        print(f"Dog Color: {self.coat_color}\n")

class Bulldog(Dog):                                            # Child class inheriting parent class
    def function(self,dog_color):
        self.dog_color = dog_color
        print("Properties of Bull dog:")
        print("Color of bull dog: ",self.dog_color)


jack = JackRussellTerrier("demo",5,"Black")                    # Object of "JackRussellTerrier" class
jack.description()                                             # Calling parent class property using child class object
jack.dogcolor("white")                                         # Calling it's own function

Bull = Bulldog("demo",2,"white")                               # Object of "Bulldog" class
Bull.get_info()                                                # Calling parent class another property using child class object
Bull.function("black")                                         # calling it's own function