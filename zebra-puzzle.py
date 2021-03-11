import itertools
import time


def zebra_puzzle_optimized():
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
  houses = first, _, middle, _, _ = [1,2,3,4,5]
  orderings = list(itertools.permutations(houses))
  return next((WATER, ZEBRA)
        for (red, green, ivory, yellow, blue) in c(orderings)
        for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
        for (dog, snails, fox, horse, ZEBRA) in c(orderings)
        for (coffee, tea, milk, oj, WATER) in c(orderings)
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
        if Englishman is red
        if Spaniard is dog
        if coffee is green
        if Ukranian is tea
        if imright(green, ivory)
        if OldGold is snails
        if Kools is yellow
        if milk is middle
        if Norwegian is first
        if nextto(Chesterfields, fox)
        if nextto(Kools, horse)
        if LuckyStrike is oj
        if Japanese is Parliaments
        if nextto(Norwegian, blue)
  )

def zebra_puzzle_normie():
    houses = first, _, middle, _, _ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in c(orderings)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )



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

def ints(start, end):
    i = start
    while (i <= end):
        yield i #Create a generator function to yield numbers
        i += 1

def c(sequence):
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item  #Create a generator function to yield items from a sequence

def instrument_fn (fn, *args):
    c.starts, c.items = 0,0
    result = fn(*args)
    print('%s got %s with %5d iterations over %7d items' % (fn.__name__, result, c.starts, c.items))

#Calculate number of iterations performed for the normal and optimized zebra puzzle function
instrument_fn (zebra_puzzle_normie) #Normal function
instrument_fn (zebra_puzzle_optimized) #Optimized solution

    
