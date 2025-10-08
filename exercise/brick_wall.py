
import math
from compas.geometry import Point
from compas.geometry import Box

# There's a data type called Brick
# that has attributes: length, width, height and a point
# and also has a rotate behavior that accepts degrees of rotation
class Brick:
    def __init__(self, xsize, ysize, zsize, point):
        self.length = xsize
        self.width = ysize
        self.height = zsize
        self.point = point
        self.rotation = 0.0

    def __str__(self):
        return f"Brick of {self.length}cm x {self.width}cm x {self.height}cm (rot: {self.rotation})"

    def draw(self):
        box = Box(self.length, self.width, self.height)
        box.frame.point = self.point
        rotation_in_radians = math.radians(self.rotation)
        box.frame.rotate(rotation_in_radians, (0, 0, 1), self.point)
        return box

    def rotate(self, rotation_in_degrees):
        self.rotation = rotation_in_degrees

