import string, re, itertools, time

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    Note that this returns only the 1st valid solution, though there might be 
    multiple possibilities."""
    for elem in fill_in(formula):
        if valid(elem):
            return elem

def faster_solve(formula):
    """"Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This is a faster method since we perform only one eval per possibility."""
    f, letters = compile_formula (formula, True)
    for digits in itertools.permutations((0,1,2,3,4,5,6,7,8,9), len(letters)):
        try:
            if f(*digits) is True:
                table = letters.maketrans(letters, ''.join(map(str,digits)))
                formula.translate(table)
        except ArithmeticError:
            pass

def compile_formula(formula, verbose = False):
    """Compile formula into a function. Also return letters found, as a str,
        in same order as params function. For example, 'YOU == ME**2'
        :returns (lambda Y,M,E,U,O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    firstletters = set(re.findall(r'\b[A-Z][A-Z]',formula)) #Find the 1st letter in a word
    parms = ','.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    if firstletters:
        test = ' and '.join(L+'!=0' for L in firstletters)
        body = '%s and (%s)' %(test, body)
    f = 'lambda %s: %s' %(parms,body)
    if verbose: print(f)
    return eval(f), letters
        
        
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

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        res = [('%s%s' %(10**i,d)) for (i,d) in enumerate(word[::-1])] #Using enumerate since it helps us keep a counter variable
        return '(' + '+' + join(res) + ')'
    else:
        return word

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
