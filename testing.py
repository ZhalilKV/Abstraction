import unittest
import math
from main import Sphere, Cylinder, Cube

class TestShape3D(unittest.TestCase):

    def test_sphere(self):
        sphere = Sphere(5)
        self.assertAlmostEqual(sphere.surface_area(), 314.16, places=2)
        self.assertAlmostEqual(sphere.volume(), 523.60, places=2)

    def test_cylinder(self):
        cylinder = Cylinder(3, 7)
        self.assertAlmostEqual(cylinder.surface_area(), 188.50, places=2)
        self.assertAlmostEqual(cylinder.volume(), 197.92, places=2)

    def test_cube(self):
        cube = Cube(4)
        self.assertEqual(cube.surface_area(), 96)
        self.assertEqual(cube.volume(), 64)

if __name__ == '__main__':
    unittest.main()