import math
from canvas.classes import Picture, Color
from line import Line

p = Picture('pic.ppm', 1024, 1024, 256)

p.colors["background"].setcolor(
        lambda x, y: 255,
        lambda x, y: 255,
        lambda x, y: 255
        )

red = p.addcolor(Color(
    lambda x, y: 255,
    lambda x, y: 0,
    lambda x, y: 0
    ))

l = Line(p, red)

for i in range(128, 192, 2):
    l.draw(i, 512, i, 768)
    l.draw(1023 - i, 512, 1023 - i, 768)

for i in range(0, 64, 2):
    l.draw(256, 384 + i, 768, 384 + i)
    l.draw(256, 832 + i, 768, 832 + i)

for i in range(91):
    sin = math.sin(math.pi * i / 180)
    cos = math.cos(math.pi * i / 180)
    l.draw(int(256 - 64 * sin), int(512 - 64 * cos), int(256 - 128 * sin), int(512 - 128 * cos))
    l.draw(int(256 - 64 * sin), int(768 + 64 * cos), int(256 - 128 * sin), int(768 + 128 * cos))
    l.draw(int(768 + 64 * sin), int(512 - 64 * cos), int(768 + 128 * sin), int(512 - 128 * cos))
    l.draw(int(768 + 64 * sin), int(768 + 64 * cos), int(768 + 128 * sin), int(768 + 128 * cos))

for i in range(0, 64, 2):
    l.draw(256 + i, 256, 256 + i, 384)
    l.draw(767 - i, 256, 767 - i, 384)

for i in range(0, 180, 2):
    sin = math.sin(math.pi * i / 180)
    cos = math.cos(math.pi * i / 180)
    l.draw(int(288 + cos * 64), int(192 + sin * 64), int(288 - cos * 64), int(192 - sin * 64))
    l.draw(int(736 + cos * 64), int(192 + sin * 64), int(736 - cos * 64), int(192 - sin * 64))

p.commit()
