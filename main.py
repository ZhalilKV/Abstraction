import random
import math
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape3D(ABC):
    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

# Sphere Class
class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

# Cylinder Class
class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

# Cube Class
class Cube(Shape3D):
    def __init__(self, side_length):
        self.side_length = side_length

    def surface_area(self):
        return 6 * (self.side_length ** 2)

    def volume(self):
        return self.side_length ** 3

def generate_random_shapes(num_shapes):
    shapes = []
    for _ in range(num_shapes):
        shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])
        if shape_type == 'Sphere':
            radius = random.randint(1, 10)
            shapes.append(Sphere(radius))
        elif shape_type == 'Cylinder':
            radius = random.randint(1, 10)
            height = random.randint(5, 20)
            shapes.append(Cylinder(radius, height))
        elif shape_type == 'Cube':
            side_length = random.randint(1, 10)
            shapes.append(Cube(side_length))
    return shapes


def display_shapes_info(shapes):
    for shape in shapes:
        print(f"Shape: {shape.__class__.__name__}")
        print(f"Surface Area: {shape.surface_area():.2f}")
        print(f"Volume: {shape.volume():.2f}")
        print("-" * 30)

# Main Execution
if __name__ == "__main__":

    try:
        num_shapes = int(input("Enter the number of random shapes to generate: "))
        if num_shapes <= 0:
            print("Please enter a positive integer.")
        else:
            random_shapes = generate_random_shapes(num_shapes)
            display_shapes_info(random_shapes)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")