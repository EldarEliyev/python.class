class Car:
    def __init__(self, brand, year, country, color):
        self.brand = brand
        self.year = year
        self.country = country
        self.color = color
        
    def display_info(self):  
        return f"Brand: {self.brand}, Year: {self.year}, Country: {self.country}, Color: {self.color}"

word = Car("Bmw", 2002, "Germain", "black")
print(word.display_info)