from picture.classes import Picture

p = Picture('pic.ppm', 1024, 1024, 511)

for pixel in p.pixels:
    pixel.color = (511 - abs(pixel.x - 511.5) // 1, 511 - abs(pixel.y - 511.5) // 1, 511 - (abs(pixel.x - 511.5) + abs(pixel.y - 511.5)) // 2)

p.commit()
