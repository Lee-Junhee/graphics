class Line:
    def oct1(pic, color, x0, y0, x1, y1):
        if (x0 > x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0 
        B = x0 - x1
        d = 2 * A + B
        while (x <= x1):
            pic.set(x, y, color)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    def oct2(pic, color, x0, y0, x1, y1):
        if (y0 > y1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = A + 2 * B
        while (y <= y1):
            pic.set(x, y, color)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    def oct7(pic, color, x0, y0, x1, y1):
        if (y1 > y0):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = A - 2 * B
        while (y >= y1):
            pic.set(x, y, color)
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B

    def oct8(pic, color, x0, y0, x1, y1):
        if (x0 > x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = 2 * A - B
        while (x <= x1):
            pic.set(x, y, color)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A

    def draw(pic, color, x0, y0, x1, y1):
        try:
            m = (y1 - y0) / (x1 - x0)
        except ZeroDivisionError:
            m = 2
        if (1 <= m):
            Line.oct2(pic, color, x0, y0, x1, y1)
        elif (0 <= m < 1):
            Line.oct1(pic, color, x0, y0, x1, y1)
        elif (-1 <= m < 0):
            Line.oct8(pic, color, x0, y0, x1, y1)
        else:
            Line.oct7(pic, color, x0, y0, x1, y1)
