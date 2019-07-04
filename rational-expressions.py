# an Expression is a tuple
# interp. An Expression is an operation on rational expression
def eval_expression(exp):
    (exp_leftmost, op, exp_rightmost) = exp
    (n1, sub_op, d1) = exp_leftmost
    (n2, opx, d2) = exp_rightmost
    if op == '+':
        return add_rat(mul_rat(n1, d2), mul_rat(n2, d1)), '/', mul_rat(d1, d2)
    if op == '-':
        return sub_rat(mul_rat(n1, d2), mul_rat(n2, d1)), '/', mul_rat(d1, d2)
    if op == '*': 
        return mul_rat(n1, n2), '/', mul_rat(d1, d2)
    else:
        return 0

def add_rat(e1, e2):
    if len(e1) == 3 and len(e2) == 3:
        (l_operand, op, r_operand) = e1
        (left_operand, opx, right_operand) = e2
        if r_operand == right_operand:
            return l_operand+left_operand, op, r_operand
        if r_operand != right_operand:
            return e1, '+', e2
        else:
            return 0
    if len(e1) == 5 and len(e2) == 5:
        (l_operand, op, r_operand, expt, num) = e1
        (left_operand, opx, right_operand, exptx, num2) = e2
        if r_operand == right_operand:
            return l_operand+left_operand, op, r_operand, expt, num
        if r_operand != right_operand:
            return e1, '+', e2
    if isinstance(e1, Number) and isinstance(e2, Number):
        return e1 + e1
    else:
        return 0

def sub_rat(e1, e2):
    if len(e1) == 3 and len(e2) == 3:
        (l_operand, op, r_operand) = e1
        (left_operand, opx, right_operand) = e2
        if r_operand == right_operand:
            return l_operand-left_operand, op, r_operand
        if r_operand != right_operand:
            return e1, '-', e2
        else:
            return 0
    if len(e1) == 5 and len(e2) == 5:
        (l_operand, op, r_operand, expt, num) = e1
        (left_operand, opx, right_operand, exptx, num2) = e2
        if r_operand == right_operand:
            return l_operand-left_operand, op, r_operand, expt, num
        if r_operand != right_operand:
            return e1, '-', e2
    if isinstance(e1, Number) and isinstance(e2, Number):
        return e1 - e1
    else:
        return 0
    
def mul_rat(e1, e2):
    (l_operand, op, r_operand) = e1
    (left_operand, op, right_operand) = e2
    if r_operand == right_operand:
        return l_operand*left_operand, op, r_operand, '**', 2
    if r_operand != right_operand:
        return 0
    else:
        return 0



    
