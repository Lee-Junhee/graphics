import math
from canvas import Picture, Color
from line import Line

p = Picture('pic.ppm', 128, 128, 255)

c = Color(
    lambda x, y: 255,
    lambda x, y: 255,
    lambda x, y: 255
    )

p.addcolor(c)

Line.draw(p, c, 0, 100, 100, 13)

p.commit()
