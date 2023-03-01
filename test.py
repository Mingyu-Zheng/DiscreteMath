'''
or   and  not
∨   ∧   ¬
'''
import logic.logic as ll
s = '(Q∧R)'
s = ll.dualreplace(s)
ll.truthtable2(s)