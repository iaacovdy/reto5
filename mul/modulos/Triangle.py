import math

from modulos.Shape import Shape, Line, Point


# Triangle class (Base for all triangle types)
class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.vertices = [p1, p2, p3]
        self.edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        self.inner_angles = self.compute_angles()

    def compute_angles(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        return [math.degrees(angle_A), math.degrees(angle_B), math.degrees(angle_C)]

    def compute_area(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def compute_perimeter(self):
        return sum(edge.length for edge in self.edges)

# Isosceles Triangle class
class Isosceles(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.is_regular = (
            self.edges[0].length == self.edges[1].length or 
            self.edges[1].length == self.edges[2].length or 
            self.edges[0].length == self.edges[2].length
        )

# Equilateral Triangle class
class Equilateral(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.is_regular = (
            self.edges[0].length == self.edges[1].length == self.edges[2].length
        )

# Scalene Triangle class
class Scalene(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.is_regular = False

# Right-Angled Triangle class
class TriRectangle(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        a, b, c = sorted([self.edges[0].length, self.edges[1].length, self.edges[2].length])
        self.is_regular = math.isclose(a**2 + b**2, c**2)
