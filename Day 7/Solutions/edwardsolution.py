class Restaurant:
    #basic properties

    def __init__(self, name, type, location):
        self.name = name
        self.type = type
        self.location = location
    
    # methods

    #serving food
    def servesFood(self, food):
        print(f"{self.name} serves {food}.")

    #serving drinks
    def servesDrinks(self, drink):
        print(f"{self.name} serves {drink}.")

    #delivers food/drinks
    def deliver(self, location):
        print(f"{self.name} delivers to {location}.")

redLobster = Restaurant("Red Lobster", "seafood restaurant", "Paramus, NJ" )

redLobster.servesFood("Lobster Linguini Alfredo")
redLobster.servesFood("Atlantic Salmon with Shrimp, Baked Potatoes and Broccoli")
redLobster.servesDrinks("Strawberry Lemonade")
redLobster.deliver("my house")