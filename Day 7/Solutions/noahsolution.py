class cookie:
    def __init__(self, type, brand,color ):
        self.type = type
        self.brand = brand
        self.color = color
        def __str__(self):
            return f"{self.brand} {self.type} cookie is {self.color}, very {self.color}"
            oreo =("oreo","dark chocolate","black")
print(oreo)