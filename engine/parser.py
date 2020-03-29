import math
from canvas import Picture, Color
from line import Line
from matrix import Matrix
from transformation import Transformation
from parametric import Parametric
from polygon import Polygon
import subprocess

def save(l, m, args):
    p.clear()
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

def parse(src, p, color):
    l = Line(p, color)
    m = Matrix()
    t = Transformation()
    param = Parametric(m, .0001)
    f = Polygon(m) 
    fxns = {
        'line': lambda args: m.addEdge((args[0], args[1], args[2]),(args[3], args[4], args[5])),
        'scale': lambda args: t.scale(args[0], args[1], args[2]),
        'move': lambda args: t.move(args[0], args[1], args[2]),
        'rotate': lambda args: t.rotate(args[0], args[1]),
        'save': lambda args: save(l, m, args),
        'circle': lambda args: param.arc((args[0], args[1], args[2]), args[3]),
        'hermite': lambda args: param.hermite((args[0], args[1]), (args[2], args[3]), (args[4], args[5]), (args[6], args[7])),
        'bezier': lambda args: param.bezier((args[0], args[1]), (args[2], args[3]), (args[4], args[5]), (args[6], args[7])),
        'box': lambda args: f.box(args[:3], args[3:6]),
        'sphere': lambda args: f.sphere(args[:3], args[3]),
        'torus': lambda args: f.torus(args[:3], args[3], args[4]),
            }
    with open(src,"r") as raw:
        commands = raw.readlines()
    cmdbuf = ''
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
            print('apply')
            t.apply(m)
            t = Transformation()
            cmdbuf = ''
        elif cmd == 'display\n':
            print('display')
            p.clear()
            l.draw(m)
            p.display()
            cmdbuf = ''
        elif cmd == 'save\n':
            cmdbuf = 'save'
        elif cmd == 'quit\n':
            break
        elif cmd == 'circle\n':
            cmdbuf = 'circle'
        elif cmd == 'hermite\n':
            cmdbuf = 'hermite'
        elif cmd == 'bezier\n':
            cmdbuf = 'bezier'
        elif cmd == 'clear\n':
            print('clear')
            m = Matrix()
            f.matrix = m
            cmdbuf = ''
        elif cmd == 'box\n':
            cmdbuf = 'box'
        elif cmd == 'sphere\n':
            cmdbuf = 'sphere'
        elif cmd == 'torus\n':
            cmdbuf = 'torus'
        elif cmd[0] == '#':
            pass
        else:
            args = cmd.split()
            fargs = list()
            for i in range(len(args)):
                try:
                    fargs.append(float(args[i]))
                except ValueError:
                    fargs.append(args[i])
            print(cmdbuf + ': ' + ','.join(args))
            fxns[cmdbuf](fargs)
            cmdbuf = ''
