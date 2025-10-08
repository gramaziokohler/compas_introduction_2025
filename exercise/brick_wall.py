
import math
from compas.geometry import Frame
from compas.geometry import Box

# There's a data type called Brick
# that has attributes: length, width, height and a point
# and also has a rotate behavior that accepts degrees of rotation
class Brick:
    def __init__(self, xsize, ysize, zsize, point):
        self.length = xsize
        self.width = ysize
        self.height = zsize
        self.frame = Frame(point, [1, 0, 0], [0, 1, 0])

    def __str__(self):
        return f"Brick of {self.length}cm x {self.width}cm x {self.height}cm (frame: {self.frame})"

    def draw(self):
        box = Box(self.length, self.width, self.height)
        box.frame = self.frame.copy()
        return box

    def rotate(self, rotation_in_degrees):
        self.frame.rotate(math.radians(rotation_in_degrees), (0, 0, 1), self.frame.point)

