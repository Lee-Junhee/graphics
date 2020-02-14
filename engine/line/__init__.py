class Line:
    pic = None
    color = -1

    def __init__(self, pic, color):
        self.pic = pic
        self.color = color

    def oct1(self, x0, y0, x1, y1):
        if (x0 > x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0 
        B = x0 - x1
        d = 2 * A + B
        while (x <= x1):
            self.pic.set(x, y, self.color)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    def oct2(self, x0, y0, x1, y1):
        if (y0 > y1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = A + 2 * B
        while (y <= y1):
            self.pic.set(x, y, self.color)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    def oct7(self, x0, y0, x1, y1):
        if (y1 > y0):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = A - 2 * B
        while (y >= y1):
            self.pic.set(x, y, self.color)
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B

    def oct8(self, x0, y0, x1, y1):
        if (x0 > x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = 2 * A - B
        while (x <= x1):
            self.pic.set(x, y, self.color)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A

    def draw(self, x0, y0, x1, y1):
        try:
            m = (y1 - y0) / (x1 - x0)
        except ZeroDivisionError:
            m = 2
        if (1 <= m):
            self.oct2(x0, y0, x1, y1)
        elif (0 <= m < 1):
            self.oct1(x0, y0, x1, y1)
        elif (-1 <= m < 0):
            self.oct8(x0, y0, x1, y1)
        else:
            self.oct7(x0, y0, x1, y1)

    def draw(self, matrix):
        matrix = matrix.getContent()
        for i in range(matrix.getEdges()):
            self.draw(matrix[0][2 * i], matrix[1][2 * i], matrix[0][2 * i + 1], matrix[1][2 * i + 1])
