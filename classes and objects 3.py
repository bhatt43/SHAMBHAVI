import math

class Solid:
    def __init__(self):
        # Accept data relevant to the solid
        pass

    def surface_area(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def volume(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

# Example 1: Cube
class Cube(Solid):
    def __init__(self, side):
        self.side = side

    def surface_area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

# Example 2: Sphere
class Sphere(Solid):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

# Example 3: Cylinder
class Cylinder(Solid):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

# Example usage
if __name__ == "__main__":
    cube = Cube(5)
    print("Cube Surface Area:", cube.surface_area())
    print("Cube Volume:", cube.volume())

    sphere = Sphere(3)
    print("Sphere Surface Area:", sphere.surface_area())
    print("Sphere Volume:", sphere.volume())

    cylinder = Cylinder(3, 7)
    print("Cylinder Surface Area:", cylinder.surface_area())
    print("Cylinder Volume:", cylinder.volume())
