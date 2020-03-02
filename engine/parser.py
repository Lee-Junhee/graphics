import math
from canvas import Picture, Color
from line import Line
from matrix import Matrix
from transformation import Transformation
import subprocess

def parse(src, p, color):
    m = Matrix()
    with open(src,"r") as raw:
        commands = raw.readlines()
    cmdbuf = ''
    t = Transformation()
    for cmd in commands:
        if cmd == 'line\n':
            cmdbuf = 'line'
        elif cmd == 'ident\n':
            t = Transformation()
            cmdbuf = ''
        elif cmd == 'scale\n':
            cmdbuf = 'scale'
        elif cmd == 'move\n':
            cmdbuf = 'move'
        elif cmd == 'rotate\n':
            cmdbuf = 'rotate'
        elif cmd == 'apply\n':
            t.apply(m)
            t = Transformation()
            cmdbuf = ''
        elif cmd == 'display\n':
            p.clear()
            l = Line(p, color)
            l.draw(m)
            p.display()
            cmdbuf = ''
        elif cmd == 'save\n':
            cmdbuf = 'save'
        elif cmd == 'quit\n':
            break
        else:
            args = cmd.split()
            if cmdbuf == 'line':
                m.addEdge((int(args[0]), int(args[1]), int(args[2])),(int(args[3]), int(args[4]), int(args[5])))
            elif cmdbuf == 'scale':
                t.scale(int(args[0]), int(args[1]), int(args[2]))
            elif cmdbuf == 'move':
                t.move(int(args[0]), int(args[1]), int(args[2]))
            elif cmdbuf == 'rotate':
                t.rotate(args[0], int(args[1]))
            elif cmdbuf == 'save':
                p.clear()
                l = Line(p, color)
                l.draw(m)
                if args[0][-4:] == '.ppm':
                    p.fname = args[0]
                    p.commit()
                else:
                    p.fname = args[0][:-4] + '.ppm'
                    p.commit()
                    subprocess.run(['convert', args[0][:-4] + '.ppm', args[0]])
                    subprocess.run(['rm', args[0][:-4]+'.ppm'])
                print(args[0])
            cmdbuf = ''
