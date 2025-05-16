class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"Your drive the {self.color} {self.model} car")
        
    def stop(self):

        print(f"Your stop the {self.model} car")
        
    def describe(self):
        print(f"{self.model} {self.year} {self.color}")
        if self.for_sale:
            print("This car is for sale")
        else:
            print("This car is not for sale")