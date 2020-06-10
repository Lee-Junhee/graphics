from subprocess import Popen, PIPE
from os import remove, fork, execlp

#constants
XRES = 2*500
YRES = 2*500
MAX_COLOR = 255
RED = 0
GREEN = 1
BLUE = 2

DEFAULT_COLOR = [0, 0, 0]

def new_screen( width = XRES, height = YRES ):
    screen = []
    for y in range( height ):
        row = []
        screen.append( row )
        for x in range( width ):
            screen[y].append( DEFAULT_COLOR[:] )
    return screen

def new_zbuffer( width = XRES, height = YRES ):
    zb = []
    for y in range( height ):
        row = [ float('-inf') for x in range(width) ]
        zb.append( row )
    return zb

def plot( screen, zbuffer, color, x, y, z ):
    newy = YRES - 1 - y
    z = int((z * 1000)) / 1000.0

    if ( x >= 0 and x < XRES and newy >= 0 and newy < YRES and zbuffer[newy][x] <= z):
        screen[newy][x] = color[:]
        zbuffer[newy][x] = z

def clear_screen( screen ):
    for y in range( len(screen) ):
        for x in range( len(screen[y]) ):
            screen[y][x] = DEFAULT_COLOR[:]

def clear_zbuffer( zb ):
    for y in range( len(zb) ):
        for x in range( len(zb[y]) ):
            zb[y][x] = float('-inf')

def condense(screen):
    s = []
    for y in range(0, len(screen), 2):
        row = []
        for x in range(0, len(screen[0]), 2):
            pixel = [0, 0, 0]
            pixel[RED] = int((screen[y][x][RED] + screen[y][x+1][RED] + screen[y+1][x][RED] + screen[y+1][x+1][RED]) / 4)
            pixel[GREEN] = int((screen[y][x][GREEN] + screen[y][x+1][GREEN] + screen[y+1][x][GREEN] + screen[y+1][x+1][GREEN]) / 4)
            pixel[BLUE] = int((screen[y][x][BLUE] + screen[y][x+1][BLUE] + screen[y+1][x][BLUE] + screen[y+1][x+1][BLUE]) / 4)
            row.append(pixel)
        s.append(row)
    while len(screen) > 0:
        screen.pop()
    for x in s:
        screen.append(x)

def save_ppm( screen, fname ):
    condense(screen)
    f = open( fname, 'w' )
    ppm = 'P3\n' + str(len(screen[0])) +' '+ str(len(screen)) +' '+ str(MAX_COLOR) +'\n'
    for y in range( len(screen) ):
        row = ''
        for x in range( len(screen[y]) ):
            pixel = screen[y][x]
            row+= str( pixel[ RED ] ) + ' '
            row+= str( pixel[ GREEN ] ) + ' '
            row+= str( pixel[ BLUE ] ) + ' '
        ppm+= row + '\n'
    f.write( ppm )
    f.close()
# def save_ppm( screen, fname ):
#     f = open( fname, 'w' )
#     ppm = 'P3\n' + str(len(screen[0])) +' '+ str(len(screen)) +' '+ str(MAX_COLOR) +'\n'
#     rows = []
#     for y in range( len(screen) ):
#         row = []
#         for x in range( len(screen[y]) ):
#             pixel = screen[y][x]
#             row.append(' '.join([str(x) for x in pixel]))
#         rows.append(' '.join(row))
#     ppm+= '\n'.join(rows)
#     print ppm
#     f.write( ppm )
#     f.close()

def save_extension( screen, fname ):
    ppm_name = fname[:fname.find('.')] + '.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def display( screen ):
    ppm_name = 'pic.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def make_animation( name ):
    name_arg = 'anim/' + name + '*'
    name = name + '.gif'
    print('Saving animation as ' + name)
    f = fork()
    if f == 0:
        execlp('convert', 'convert', '-delay', '1.7', name_arg, name)
