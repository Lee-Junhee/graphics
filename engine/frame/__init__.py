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
        
        self.addPoint()
