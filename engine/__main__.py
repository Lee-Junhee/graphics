import math
from canvas.classes import Picture, Color
from line import Line

p = Picture('pic.ppm', 1024, 1024, 256)

lineColor = p.addcolor(Color(
    lambda x, y: 0 + (x + y) // 8,
    lambda x, y: 256 - (x + y) // 8,
    lambda x, y: abs(256 - (x + y) // 4)
    ))

l = Line(p, lineColor)

for i in range(0, 512, 7):
    l.draw(i, 511, 511, 511 - i)
    l.draw(512, i, 512 + i, 511)
    l.draw(1023 - i, 512, 512, 512 + i)
    l.draw(512, 1023 - i, 511 - i, 512)

p.commit()
