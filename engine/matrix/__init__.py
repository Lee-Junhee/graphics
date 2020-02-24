class Matrix:
    edges = -1
    content = None

    def multiply(m1, m2):
        #matrix multiplication code here
        for i in range(len(m2.content[0])):
            col = [[0], [0], [0], [0]]
            for j in range(4):
                for k in range(4):
                    col[k][0] += m1.content[k][j] * m2.content[j][i]
            for j in range(4):
                m2.content[j][i] = col[j][0]

    def __init__(self):
        self.content = [[], [], [], []]
        self.edges = 0

    def __init__(self, *points):
        self.content = [[], [], [], []]
        self.edges = 0
        for point in points:
            self.addPoint(point)

    def getEdges(self):
        return int(self.edges)

    def addPoint(self, point):
        self.edges += 0.5
        for i in range(3):
            self.content[i].append(point[i])
        self.content[3].append(1)

    def addEdge(self, p1, p2):
        if self.getEdges() != self.edges:
            self.addPoint((self.content[0][-1], self.content[1][-1], self.content[2][-1]))
        self.addPoint(p1)
        self.addPoint(p2)

    def ident(self):
        self.content = [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
                ]

    def print(self):
        for i in range(4):
            for j in self.content[i]:
                print("%.2f" % j, end = "\t", flush=True)
            print("")
