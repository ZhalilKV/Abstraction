Shape3D Project
This project demonstrates the concept of abstraction in Python using an abstract base class for 3D shapes. It includes various shape classes that implement methods to calculate surface area and volume, showcasing how abstraction and polymorphism allow treating different shapes through the same interface.

Abstract Base Class
The Shape3D class is defined as an abstract base class using Python's abc module. It includes two abstract methods:

surface_area(): Returns the surface area of the shape.
volume(): Returns the volume of the shape.
3D Shape Subclasses
The following subclasses of Shape3D are implemented:

Sphere
Surface Area: 4*pi*r^2
Volume: (4/3)pi*r^3)
Cylinder
Surface Area: 2*pi*r(r + h)
Volume: pi*r^2*h
Cube
Surface Area: 6*a^2
Volume: a^3

SAMPLE OUTPUT
![Screenshot 2025-04-24 140435](https://github.com/user-attachments/assets/d8a3b81c-6c96-4637-9e4f-e9e1c264b485)

TESTING SCREENSHOT
![Screenshot 2025-04-24 140435](https://github.com/user-attachments/assets/9029371b-982e-45fd-b727-740a6a1b16ef)
![Screenshot 2025-04-24 140353](https://github.com/user-attachments/assets/e08bd8d1-1447-4f71-9690-8a65d733b4ac)

