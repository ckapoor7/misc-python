"""
@author: chaitanya
"""
import random

# This builds a deck of 52 cards. 
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 
def deal(numhands, n=5, deck=mydeck):
    """Shuffle the deck and deal out numhands n-card hands """
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range (numhands)]

def hand_percentages(n = 700*1000):
    """ Sample n random hands and print a table of percentages
        for each type of hand."""
    counts = [0] * 9;
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1;
    for i in reversed(range(9)):
        print('%14s: %6.3f'%(hand_names[i], 100.*counts[i]/n));

def poker(hands):
    """Return the list of winning hands: poker([hand,...]) => hand"""
    return allmax(hands,key=hand_rank)

def allmax(iterable, key=None):
    """Returns a list of all items equal to the max of the iterable"""
    max_hand = max(iterable,key=hand_rank)
    i = 0
    all_hands = []
    for item in iterable:
        if (hand_rank(item) == hand_rank(max_hand)):
            all_hands.append(item)            
    return all_hands

def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    ranks = card_ranks(hand)
    
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return  (6, kind(3,ranks), kind(2,ranks))
    elif flush(hand):                              # flush
        return (5,ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3,kind(3,ranks),ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2,two_pair(ranks),ranks)
    elif kind(2, ranks):                           # kind
        return (1,kind(2,ranks),ranks)
    else:                                          # high card
        return (0,ranks)
    
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    high_pair = kind(2,ranks) #Select highest pair
    low_pair = kind(2,list(reversed(ranks))) #Select the lowest pair
    if high_pair != low_pair:
        return (high_pair,low_pair)
    else:
        return None
    
    
def card_ranks(hand):
    """Returns a list of the ranks, sorted with higher first"""
    ranks = ['--23456789TJQA'.index(r) for r,s in hand] #Iterate over the ranks and suit, but only store rank
    ranks.sort(reverse = True) #Sort in descending order
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks #Account for a straight low

def straight(ranks):
    """Return true if the ordered ranks form a 5-card straight"""
    return (max(ranks)-min(ranks)==4) and len(set(ranks)) == 5

def flush(hand):
    """Return true if all the cards have the same suit"""
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank
    return None
    
    """
    Alternate:
    freq = {}
    for rank in ranks:
        if (rank in freq):
            freq[rank] += 1
        else:
            freq[rank] = 1
    for elem in freq:
        if (freq[elem]==n):
            return elem
    return None"""
    

def test():
    """Test cases for the functions in poker program."""
    sf = "6C 7C 8C 9C TC".split() #Straight flush
    fk = "9D 9H 9S 9C 7D".split() #Four of a kind
    fh = "TD TC TH 7C 7D".split() #Full house
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert card_ranks(sf)
    assert straight([9,8,7,6,5]) == True
    assert straight([9,8,8,6,5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
   # assert poker([sf, fk, fh]) == sf
   # assert poker([fk, fh]) == fk
    #assert poker([fh, fh]) == fh
   # assert poker([sf]) == sf
    #assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "tests pass"

print (test())

