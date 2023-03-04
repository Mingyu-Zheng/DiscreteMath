# coding=utf-8
'''
or   and  not
∨   ∧   ¬
'''

# ch1
def dualformula(s):
    s1 = s.replace('∨', '|')
    s1 = s.replace('∧', '∨')
    s1 = s.replace('|','∧')
    s1 = s.replace('0', 'F')
    s1 = s.replace('1', '0')
    s1 = s.replace('F','1')
    return s1

# ch2
# ch2-1
def print01(truthtable):
    for tv in truthtable:
        if tv:
            print("1", end="   ")
        else:
            print("0", end="   ")
    print("")
    return

def truthtable2(s):
    w = 'Q   R   '+s
    print("%r"%w)
    truth = {True, False}
    for Q in truth:
        for R in truth:
            f = eval(s)
            t = [Q, R]+[f]
            print01(t)
    return

def truthtable3(s):
    w = 'P   Q   R   '+s
    print("%r"%w)
    truth = {True, False}
    for P in truth:
        for Q in truth:
            for R in truth:
                f = eval(s)
                t = [P, Q, R]+[f]
                print01(t)
    return

# ch2-2
def isargument2(pre, s):
    w='Q   R   '
    for u in pre:
        w = w + u + '   '
    w = w + '╞   ' + s
    print(w)
    truth = {True, False}
    for Q in truth:
        for R in truth:
            pv = []
            for pk in pre:
                pv = pv + [eval(pk)]
            f = eval(s)
            t = [Q, R] + pv + [f]
            print01(t)
    return

def isargument3(pre, s):
    w='P   Q   R   '
    for u in pre:
        w = w + u + '   '
    w = w + '╞' + s
    print(w)
    truth = {True, False}
    for P in truth:
        for Q in truth:
            for R in truth:
                pv = []
                for pk in pre:
                    pv = pv + [eval(pk)]
                f = eval(s)
                t = [P, Q, R] + pv + [f]
                print01(t)
    return

def isequation2(e1, e2):
    w='Q   R   '+e1+'   '+e2+'   e1==e2'
    print(w)
    truth = {True, False}
    for Q in truth:
        for R in truth:
            f1 = eval(e1)
            f2 = eval(e2)
            t = [Q, R] + [f1, f2] + [f1 == f2]
            print01(t)
    return

def isequation3(e1, e2):
    w='P   Q   R   '+e1+'   '+e2+'   e1==e2'
    print(w)
    truth = {True, False}
    for P in truth:
        for Q in truth:
            for R in truth:
                f1 = eval(e1)
                f2 = eval(e2)
                t = [P, Q, R] + [f1, f2] + [f1 == f2]
                print01(t)
    return

# ch2-3
def issubstitution2(s, t, s1):
    w='Q   R   f1   f2   f1==f2'
    print("%r"%w)
    rv = [s, t, s1]
    truth = {True, False}
    for Q in truth:
        for R in truth:
            f1 = eval(s.replace(t, s1))
            v = str(eval(s1))
            f2 = eval(s.replace(t, v))
            tv = [Q, R] + [f1, f2] + [f1 == f2]
            print01(tv)
    return

def issubstitution3(s ,t ,s1):
    w='P   Q   R   f1  f2  f1==f2'
    print("%r"%w)
    rv = [s, t, s1]
    truth = {True, False}
    for P in truth:
        for Q in truth:
            for R in truth:
                f1 = eval(s.replace(t, s1))
                v = str(eval(s1))
                f2 = eval(s.replace(t, v))
                tv = [Q, R] + [f1, f2] + [f1 == f2]
                print01(tv)
    return

def invassignment(s):
    s = s.replace('P', '(¬P)')
    s = s.replace('Q', '(¬Q)')
    s = s.replace('R', '(¬R)')
    return s

def dualreplace(s):
    s = s.replace('∨', ' or ')
    s = s.replace('∧', ' and ')
    s = s.replace('¬', ' not ')
    return s


