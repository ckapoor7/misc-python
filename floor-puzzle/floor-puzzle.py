#The problem description is in the README.MD file

import itertools

def adjacent(floor1, floor2):
    "Check for adjacent floors "
    return abs(floor1-floor2)==1

def floor_puzzle():
    possible_floors = bottom, _, _, _, top = [1,2,3,4,5]
    #Define a generator function to match the required conditions
    gen = ([Hopper, Kay, Liskov, Perlis, Ritchie]
           for Hopper, Kay, Liskov, Perlis, Ritchie in itertools.permutations(possible_floors)
           if Hopper != top
           if Kay != bottom
           if Liskov != top and Liskov != bottom
           if Perlis > Kay
           if not adjacent(Ritchie, Liskov)
           if not adjacent(Liskov, Kay))
    return next(gen)

print(floor_puzzle())
