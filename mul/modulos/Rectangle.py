import math

from modulos.Shape import Shape, Line, Point

# Rectangle class
class Rectangle(Shape):
    def __init__(self, p1, p2, p3, p4):
        super().__init__()
        self.vertices = [p1, p2, p3, p4]
        self.edges = [Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)]
        self.is_regular = (
            self.edges[0].length == self.edges[2].length and 
            self.edges[1].length == self.edges[3].length
        )

    def compute_area(self):
        return self.edges[0].length * self.edges[1].length
    
    def compute_perimeter(self):
        return 2 * (self.edges[0].length + self.edges[1].length)

# Square class
class Square(Rectangle):
    def __init__(self, p1, p2, p3, p4):
        super().__init__(p1, p2, p3, p4)
        if self.edges[0].length != self.edges[1].length:
            raise ValueError("All sides must be equal for a square")

    def compute_area(self):
        return self.edges[0].length ** 2
    
    def compute_perimeter(self):
        return 4 * self.edges[0].length