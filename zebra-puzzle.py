import itertools
import time


def zebra_puzzle():
  """
  There are five houses.
The Englishman lives in the red house.
The Spaniard owns the dog.
Coffee is drunk in the green house.
The Ukrainian drinks tea.
The green house is immediately to the right of the ivory house.
The Old Gold smoker owns snails.
Kools are smoked in the yellow house.
Milk is drunk in the middle house.
The Norwegian lives in the first house.
The man who smokes Chesterfields lives in the house next to the man with the fox.
Kools are smoked in the house next to the house where the horse is kept.
The Lucky Strike smoker drinks orange juice.
The Japanese smokes Parliaments.
The Norwegian lives next to the blue house.
"""

  houses = first, _, middle, _,_ =[1 ,2 ,3 ,4 ,5]
  orderings = list(itertools.permutations(houses))
  g = ((ZEBRA, WATER)
    for red, green, ivory, yellow, blue in c(orderings)
    for Englishman, Spaniard, Ukrainian, Norwegian, Japanese in c(orderings)
    for dog, snails, fox, horse, ZEBRA in c(orderings)
    for tea, coffee, milk,orange,WATER in c(orderings)
    for OldGoldSmoker, Kools, Chesterfields,LuckyStrike,parliaments in c(orderings)
    if red is Englishman
    if dog is Spaniard
    if coffee is green
    if Ukrainian is tea
    if is_right_of(green, ivory)
    if OldGoldSmoker is snails
    if Kools is yellow
    if milk is middle
    if Norwegian is first
    if is_next_to(Chesterfields, fox)
    if is_next_to(Kools, horse)
    if LuckyStrike is orange
    if Japanese is parliaments
    if Norwegian is blue)

  return next(g)


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, results

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int): #Check for an integer type
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)
