import math

class Parametric:
    step = -1
    edges = None

    def __init__(self, edgeMatrix, step=0.01):
        self.edges = edgeMatrix
        self.step = step

    def arc(self, center, radius, angle=2*math.pi):
        x = lambda t: center[0] + radius * math.cos(angle / t)
        y = lambda t: center[1] + radius * math.sin(angle / t)
        self.add(x, y)

    def hermite(self, p0, p1, r0, r1):
        x = lambda t: 
        self.add(x, x)

    def add(self, x, y)
        t = 0
        while t < 1:
            self.addEdge((x(t), y(t), 0), (x(min(t + step, 1)), y(min(t + step, 1), 0)))
            t += step
