# coding=utf-8
'''
or   and  not
∨   ∧   ¬
'''
import logic.logic as ll

# 题目1：用真值表验证 ╞((Q∧(Q→R))→R)
'''
示例输出：
'Q   R   (not (Q and ((not Q) or R))) or R'
0   0   1   
0   1   1
1   0   1
1   1   1
'''
def question1():
    s = '(not (Q and ((not Q) or R))) or R'
    # ====== answer-sheet-begin =======
    ll.truthtable2(s)
    # ======  answer-sheet-end  =======

# 题目2：用真值表验证 P,(Q→(P→R))╞(Q→R)
'''
示例输出：
P   Q   R   P   (not Q) or ((not P) or R)   ╞(not Q) or R
0   0   0   0   1   1   
0   0   1   0   1   1
0   1   0   0   1   0
0   1   1   0   1   1
1   0   0   1   1   1
1   0   1   1   1   1
1   1   0   1   0   0
1   1   1   1   1   1
'''
def question2():
    pre = ['P','(not Q) or ((not P) or R)']
    # ====== answer-sheet-begin =======
    s = '(not Q) or R'
    ll.isargument3(pre, s)
    # ======  answer-sheet-end  =======


# 题目3：在Python中验证替换式s1=s[r1/r2]，其中s=(Q→(R→R)),r1=(R→R),r2=(R→(Q→R))
'''
示例输出：
'Q   R   f1   f2   f1==f2'
0   0   1   1   1   
0   1   1   1   1
1   0   1   1   1
1   1   1   1   1
'''
def question3():
    s = '(not Q) or ((not R) or R)'
    # ====== answer-sheet-begin =======
    r1 = '(not R) or R'
    r2 = '(not R) or ((not Q) or R)'
    ll.issubstitution2(s, r1, r2)
    # ======  answer-sheet-end  =======


# 题目4：实现一个函数，完成三元命题变元合式公式等价性判断，e1，e2为合式公式，如二者等价返回值为True，否则为False
'''
示例输出：
True
False
'''
def question4():
    def isequation3(e1, e2):
    # ====== answer-sheet-begin =======
        truth = {True, False}
        for P in truth:
            for Q in truth:
                for R in truth:
                    f1 = eval(e1)
                    f2 = eval(e2)
                    if f1 != f2:
                        return False
        return True
    # ======  answer-sheet-end  =======

    e1 = '(not (P and Q)) or R'
    e2 = '(not P) or ((not Q) or R)'
    print(isequation3(e1, e2))
    e1 = '(not P) or (Q or R)'
    e2 = '(not (Q or R)) or P'
    print(isequation3(e1, e2))
