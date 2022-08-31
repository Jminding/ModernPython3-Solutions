class Bunny:

    def __init__(self, name, gender, breed, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
    
    def hops(self):
        print(f"{self.name} hops.")

    def multi_hops(self, tms):
        print(f"{self.name} hops " + f"{tms}" + " more times.")

    def lay_down(self):
        print(f"{self.name} lays down.")

    def eat(self, food):
        print(f"{self.name} eats {food}")
    
    def drink(self, liquid):
        print(f"{self.name} drinks {liquid}")

    def self_intro(self):
        print(f"{self.name} is a {self.gender}, {self.breed} bunny that is {self.age}-month old.")

    




n = input("Choose a name for your bunny: ")
g = input("Choose a gender for your bunny: ")
b = input("Choose a breed for your bunny: ")
a = input("Choose an age for your bunny: ")
ab = Bunny(n,g,b,a)

ab.self_intro()

ab.hops()

ab.multi_hops(5)

ab.eat("carrots")

ab.drink("water")

ab.lay_down()