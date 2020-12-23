class Polygon():

    def __init__(self, sides_number):
        self.sides_number = sides_number


    def insert_sides(self):
        self.sides = [float(input(f"Insert side №{i+1}:")) 
            for i in range(self.sides_number)]

class Rectangle(Polygon):

    def __init__(self):
        super().__init__(2)

    def rectangle_area(self):
        a, b = self.sides
        return a*b


rect = Rectangle()

rect.insert_sides()
print(rect.rectangle_area())