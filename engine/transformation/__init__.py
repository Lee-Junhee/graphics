from matrix import Matrix
from math import cos, sin, pi

class Transformation():
    transform = None

    r = {
            "x": [1, 2],
            "y": [3, 1],
            "z": [0, 1],
            }

    def __init__(self):
        self.transform = Matrix()
        self.transform.ident()

    def scale(self, sx=1, sy=1, sz=1):
        dilation = Matrix()
        dilation.ident()
        factor = [sx, sy, sz]
        for i in range(3):
            dilation.content[i][i] = factor[i]
        Matrix.multiply(dilation, self.transform)

    def move(self, tx=0, ty=0, tz=0):
        translation = Matrix()
        translation.ident()
        addend = [tx, ty, tz]
        for i in range(3):
            translation.content[i][3] = addend[i]
        Matrix.multiply(translation, self.transform)
    
    def rotate(self, axis="z", angle=0):
        r = self.r
        angle = angle * pi / 180
        rotation = Matrix()
        rotation.ident()
        rotation.content[r[axis][0]][r[axis][0]] = cos(angle)
        rotation.content[r[axis][1]][r[axis][0]] = -sin(angle)
        rotation.content[r[axis][0]][r[axis][1]] = sin(angle)
        rotation.content[r[axis][1]][r[axis][1]] = cos(angle)
        Matrix.multiply(rotation, self.transform)

    def apply(self, content):
        Matrix.multiply(self.transform, content)
