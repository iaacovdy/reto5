from modulos.Shape import *
from modulos.Triangle import *
from modulos.Rectangle import *


def main():
    
    # Example usage:
    p1 = Point(0, 0)
    p2 = Point(5, 0)
    p3 = Point(5, 5)
    p4 = Point(0, 5)

    # Square
    square = Square(p1, p2, p3, p4)
    print(f"Square area: {square.compute_area()}")        # Output: 25
    print(f"Square perimeter: {square.compute_perimeter()}")  # Output: 20

    # Triangle
    t1 = Point(0, 0)
    t2 = Point(4, 0)
    t3 = Point(4, 3)
    triangle = TriRectangle(t1, t2, t3)
    print(f"Triangle area: {triangle.compute_area()}")         # Output: 6.0
    print(f"Triangle perimeter: {triangle.compute_perimeter()}")  # Output: 12.0
        
    
if __name__ == '__main__':
    main()