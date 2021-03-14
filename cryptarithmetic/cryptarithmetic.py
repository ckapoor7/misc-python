import string, re, itertools, time

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    Note that this returns only the 1st valid solution, though there might be 
    multiple possibilities."""
    for elem in fill_in(formula):
        if valid(elem):
            return elem

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]', formula))) #Single occurence of all letters in formula
    for digits in itertools.permutations('1234567890', len(letters)):
        table = letters.maketrans(letters, ''.join(digits)) #Join the tuples to make a big string
        yield formula.translate(table)
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

"""A bunch of test cases, which some not-so-trivial
   ones (ie - hard to solve by hand)."""


examples = """YOU == ME**2
TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
PLUTO not in set([PLANETS])""".splitlines()

def timedcall(fn, *args):
    """ Call function and return elapsed time """
    t0 = time.process_time()
    res = fn(*args)
    t1 = time.process_time()
    return t1 - t0, res

def test(func, example):
    "Test our functions with the above examples "
    t = time.process_time()
    for elem in example:
        print(); print(13*' ', elem)
        print('%6.4f sec: %s' % timedcall(func, elem))
    print('Total time: %6.4f' %(time.process_time()-t))

test(solve, examples)    
