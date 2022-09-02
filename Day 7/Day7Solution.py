class VendingMachineTooBigError(Exception):
    
    def __init__(self):
        super()
    
    def __repr__(self):
        return "Vending machine too big!"
    
    def __str__(self):
        return self.__repr__()
    
class ItemNotFoundError(Exception):

    def __init__(self):
        super()

    def __repr__(self):
        return "Item not in vending machine!"
    
    def __str__(self):
        return self.__repr__()

class Drink:
    """A drink"""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} -> ${self.price:.2f}"
    
    def __str__(self):
        return self.__repr__()

class VendingMachine:
    """A literal vending machine"""

    def __init__(self, rows: int, cols: int) -> None:
        if rows > 9 or cols > 9:
            raise VendingMachineTooBigError
        self.rows = rows
        self.cols = cols
        self.items = []
        for i in range(rows):
            self.items.append([])
            for _ in range(cols):
                self.items[i].append({})
    
    def fill_spot(self, drink: Drink, slot: int, number: int) -> None:
        try:
            slot = str(slot).lstrip("0")
            if len(slot) > 3:
                print("Invalid spot.")
                raise ItemNotFoundError
            r = int(slot[0]) - 1
            c = int(slot[1:])
            self.items[r][c][drink] = number
        except Exception:
            print("Invalid spot.")
            print(ItemNotFoundError)
        
    def buy(self, slot: int) -> None:
        try:
            slot = str(slot).lstrip("0")
            if len(slot) > 3:
                print("Invalid spot.")
                raise ItemNotFoundError
            r = int(slot[0]) - 1
            c = int(slot[1:])
            self.items[r][c][list(self.items[r][c].keys())[0]] -= 1
            print(f"That will be ${list(self.items[r][c].keys())[0].price:.2f}.")
        except Exception:
            print("Invalid spot.")
            print(ItemNotFoundError().__str__())

    def __repr__(self):
        ret = ""
        for i in range(len(self.items)):
            for j in range(len(self.items[i])):
                ret += f"{int(j.__str__()) + (i + 1) * 100}: {self.items[i][j]} "
            if i != len(self.items) - 1:
                ret += "\n"
        return ret
    
    def __str__(self):
        return self.__repr__()

def main():
    vending_machine = VendingMachine(9, 9)
    vending_machine.fill_spot(Drink("Sprite", 2.00), 100, 2)
    vending_machine.fill_spot(Drink("Ginger Ale", 3.00), 101, 50)
    print(vending_machine)
    print()
    vending_machine.buy(100)
    print()
    vending_machine.buy(99)
    print(vending_machine)

if __name__ == "__main__":
    main()