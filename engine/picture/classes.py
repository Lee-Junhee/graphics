class Picture:
    fname = ''
    width = -1
    height = -1
    depth = -1
    pixels = []

    def __init__(self, fname):
        self.fname = fname
        with open(fname, 'r') as pic:
           raw = read(pic)
           data = raw.split()
           self.width = data[1]
           self.height = data[2]
           self.depth = data[3]
           self.pixels = Picture.load(data[4:], data[1], data[2], 0)

    def load(data, width, height, index):
        if len(data) == 0:
            return []
        else:
            return [Pixel(index % width, index // height, (data[0], data[1], data[2]))] + Picture.load(data[3:], width, height, index + 1)

    def __init__(self, fname, width, height, depth):
        self.fname = fname
        self.width = width
        self.height = height
        self.depth = depth
        for x in range(width):
            for y in range(height):
                self.pixels += [Pixel(x, y, (0, 0, 0))]

    def commit(self):
        with open(self.fname, 'w+') as pic:
            pic.write('P3\n')
            pic.write("{width} {height}\n".format(width=self.width, height=self.height))
            pic.write("{depth}\n".format(depth=self.depth))
            for pixel in self.pixels:
                pic.write(pixel.value())
                pic.write("\n")

class Pixel:
    x = -1
    y = -1
    color = (-1, -1, -1)

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def value(self):
        color = self.color
        return "%d %d %d" % (color[0], color[1], color[2])
