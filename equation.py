import math

constants = {'pi': math.pi, 'e': math.e}

fxns = ['log', 'sin', 'cos', 'tan']

fxn = lambda x: 0

def addition(a, b):
    return lambda x: a(x) + b(x)

def subtraction(a, b):
    return lambda x: a(x) - b(x)

def multiplication(a, b):
    return lambda x: a(x) * b(x)

def division(a, b):
    return lambda x: a(x) / b(x)

def exponentiation(a, b):
    return lambda x: a(x) ** b(x)

def modulo(a, b):
    return lambda x: a(x) % b(x)

def logarithm(a):
    return lambda x: math.log(a(x))

def sine(a):
    return lambda x: math.sin(a(x))

def cosine(a):
    return lambda x: math.cos(a(x))

def tangent(a):
    return lambda x: math.tan(a(x))

def parse(eqstr):
    eq = []
    term = ''
    for x in eqstr + 'a':
        if term == '':
            term = x
        elif term in ['+', '-', '/', '%', '(', ')']:
            eq.append(term)
            term = x
        elif term == '*':
            if x == '*':
                eq.append('**')
                term = ''
            else:
                eq.append('*')
                term = x
        elif term[0] in '0123456789':
            if x in '0123456789':
                term += x
            else:
                eq.append(number(term))
                term = x
        elif term in constants:
            eq.append(number(constants[term]))
            term = x
        elif term == 'x':
            eq.append(lambda y: y)
            term = x
        elif term in fxns:
            eq.append(term)
            term = x
        else:
            term += x
    solve(eq)
    return eq[0]

def number(value):
    val = int(value)
    return lambda x: val

def solve(eq, start=0):
    #parenthesis code
    try:
        o = eq.index('(', start)
    except ValueError:
        o = -1
    if o != -1:
        eq.pop(o)
        solve(eq, o)
    try:
        c = eq.index(')', start)
        eq.pop(c)
    except ValueError:
        c = len(eq)
    #unary operations
    while True:
        done = True
        try:
            i = eq.index('log', start, c)
            eq.pop(i)
            eq.insert(i, logarithm(eq.pop(i)))
            c -= 1
            done = False
        except ValueError:
            pass
        try:
            i = eq.index('sin', start, c)
            eq.pop(i)
            eq.insert(i, sine(eq.pop(i)))
            c -= 1
            done = False
        except ValueError:
            pass
        try:
            i = eq.index('cos', start, c)
            eq.pop(i)
            eq.insert(i, cosine(eq.pop(i)))
            c -= 1
            done = False
        except ValueError:
            pass
        try:
            i = eq.index('tan', start, c)
            eq.pop(i)
            eq.insert(i, tangent(eq.pop(i)))
            c -= 1
            done = False
        except ValueError:
            pass
        if done:
            break
    #exponentiation
    exp = []
    for i in range(start, c):
        if eq[i] in ['^', '**']:
            exp.append(i)
    while len(exp) > 0:
        i = exp.pop(0)
        eq.pop(i)
        eq.insert(i - 1, exponentiation(eq.pop(i - 1), eq.pop(i - 1)))
        c -= 2
        for x in range(len(exp)):
            exp.insert(x, exp.pop(x) - 2)
    #multiplication and division and modulo
    ind = []
    for i in range(start, c):
        if eq[i] in ['*', '/', '%']:
            ind.append(i)
    while len(ind) > 0:
        i = ind.pop(0)
        f = eq.pop(i)
        if f == '*':
            eq.insert(i - 1, multiplication(eq.pop(i - 1), eq.pop(i - 1)))
        elif f == '/':
            eq.insert(i - 1, division(eq.pop(i - 1), eq.pop(i - 1)))
        else:
            eq.insert(i - 1, modulo(eq.pop(i - 1), eq.pop(i - 1)))
        c -= 2
        for x in range(len(ind)):
            ind.insert(x, ind.pop(x) - 2)
    #addition and subtraction
    ind = []
    for i in range(start, c):
        if eq[i] in ['+', '-']:
            ind.append(i)
    while len(ind) > 0:
        i = ind.pop(0)
        f = eq.pop(i)
        if f == '+':
            eq.insert(i - 1, addition(eq.pop(i - 1), eq.pop(i - 1)))
        else:
            eq.insert(i - 1, subtraction(eq.pop(i - 1), eq.pop(i - 1)))
        c -= 2
        for x in range(len(ind)):
            ind.insert(x, ind.pop(x) - 2)