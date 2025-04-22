import math

class Shape:
    def __init__(self):
        # Base class doesn't hold data
        pass

    def perimeter(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def area(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

# Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

# Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

# Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius  # Circumference

    def area(self):
        return math.pi * self.radius ** 2

# Equilateral Triangle
class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 3 * self.side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

# Example usage
if __name__ == "__main__":
    square = Square(4)
    print("Square Perimeter:", square.perimeter())
    print("Square Area:", square.area())

    rectangle = Rectangle(5, 3)
    print("Rectangle Perimeter:", rectangle.perimeter())
    print("Rectangle Area:", rectangle.area())

    circle = Circle(2.5)
    print("Circle Circumference:", circle.perimeter())
    print("Circle Area:", circle.area())

    triangle = EquilateralTriangle(6)
    print("Triangle Perimeter:", triangle.perimeter())
    print("Triangle Area:", triangle.area())
