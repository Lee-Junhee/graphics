from math import pi, cos, sin

class Frame:
    edges = None
    step = -1

    def __init__(self, edges, step=0.01):
        self.edges = edges
        self.step = step

    def addPoint(self, point):
        m = self.edges
        m.addEdge(point, point)
    
    def box(self, corner, dim):
        m = self.edges
        m.addEdge(corner, (corner[0] + dim[0], corner[1], corner[2]))
        m.addEdge(corner, (corner[0], corner[1] - dim[1], corner[2]))
        m.addEdge(corner, (corner[0], corner[1], corner[2] - dim[2]))
        m.addEdge((corner[0], corner[1] - dim[1], corner[2] - dim[2]),
                (corner[0], corner[1], corner[2] - dim[2]))
        m.addEdge((corner[0], corner[1] - dim[1], corner[2] - dim[2]),
                (corner[0], corner[1] - dim[1], corner[2]))
        m.addEdge((corner[0], corner[1] - dim[1], corner[2] - dim[2]),
                (corner[0] + dim[0], corner[1] - dim[1], corner[2] - dim[2]))
        m.addEdge((corner[0] + dim[0], corner[1] - dim[1], corner[2]),
                (corner[0], corner[1] - dim[1], corner[2]))
        m.addEdge((corner[0] + dim[0], corner[1] - dim[1], corner[2]),
                (corner[0] + dim[0], corner[1], corner[2]))
        m.addEdge((corner[0] + dim[0], corner[1] - dim[1], corner[2]),
                (corner[0] + dim[0], corner[1] - dim[1], corner[2] - dim[2]))
        m.addEdge((corner[0] + dim[0], corner[1], corner[2] - dim[2]),
                (corner[0], corner[1], corner[2] - dim[2]))
        m.addEdge((corner[0] + dim[0], corner[1], corner[2] - dim[2]),
                (corner[0] + dim[0], corner[1], corner[2]))
        m.addEdge((corner[0] + dim[0], corner[1], corner[2] - dim[2]),
                (corner[0] + dim[0], corner[1] - dim[1], corner[2] - dim[2]))

    def sphere(self, center, radius):
        x = lambda theta: radius * cos(theta * 2 * pi) + center[0]
        y = lambda theta, phi: radius * sin(theta * 2 * pi) * cos(phi * pi) + center[1]
        z = lambda theta, phi: radius * sin(theta * 2 * pi) * sin(phi * pi) + center[2]
        for theta in range(0, 1, self.step):
            for phi in range(0, 1, self.step):
                self.addPoint((x(theta), y(theta, phi), z(theta, phi)), (x(theta), y(theta, phi), z(theta, phi)))

    def torus(self, center, radius1, radius2):
        x = lambda theta, phi: cos(phi * 2 * pi) * (radius1 * cos(theta * 2 * pi) + radius2) + center[0]
        y = lambda theta: radius1 * sin(theta * 2 * pi) + center[1]
        z = lambda theta, phi: - sin(phi * 2 * pi) * (radius1 * cos(theta * 2 * pi) + radius2) + center[2]
        for theta in range(0, 1, self.step):
            for phi in range(0, 1, self.step):
                self.addPoint((x(theta, phi), y(theta), z(theta, phi)), (x(theta, phi), y(theta), z(theta, phi)))

