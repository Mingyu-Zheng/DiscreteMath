# coding=utf-8
'''
or   and  not
∨   ∧   ¬
'''
import logic.logic as ll

# 题目1：用真值表验证 ╞((Q∧(Q→R))→R)
'''
示例输出：
'Q   R   ( not (Q & (( not Q) | R))) | R'
0   0   1   
0   1   1
1   0   1
1   1   1
'''
def question1():
    s = '(¬(Q∧((¬Q)∨R)))∨R'
    # ====== answer-sheet-begin =======
    s = ll.dualreplace(s)
    ll.truthtable2(s)
    # ======  answer-sheet-end  =======

# 题目2：用真值表验证 P,(Q→(P→R))╞(Q→R)
'''
示例输出：
P   Q   R   P   ( not Q) | (( not P) | R)   ╞ not Q | R
0   0   0   1   1   
0   1   0   1   0
1   0   0   1   0
1   1   0   1   0
0   0   1   1   1
0   1   1   1   0
1   0   1   0   0
1   1   1   1   0
'''
def question2():
    pre = ['P','(¬Q)∨((¬P)∨R)']
    s = '¬Q∨R'
    # ====== answer-sheet-begin =======
    pre = [ll.dualreplace(item) for item in pre]
    s = ll.dualreplace(s)
    ll.isargument3(pre, s)
    # ======  answer-sheet-end  =======

