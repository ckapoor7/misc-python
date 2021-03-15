"""A naive approach to find a sub-palindrome in a string would be to run
   three loops to determine our result. Quite obviously, a O(n^3) approach
   isn't the most efficient way to solve this problem. Here, I attempt to try
   a more efficient algorithm."""

def grow(text, start, end):
    """Start with a 0- or 1- length palindrome in order to "grow" to a 
    to a potentially bigger one (Our basic objective is to start from the middle
    and move outwards."""
    while (start > 0 and end < len(text)
           and text[start-1].upper() == text[end].upper()):
        start -= 1; end += 1
    return (start,end)

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0,0) #Empty string
    def length(slice): a,b = slice; return b-a
    possible_res = [grow(text, start, end)
                  for start in range (len(text))
                  for end in (start, start+1)]
    return max(possible_res, key = length) #Return the longest sub-palindrome

#A bunch of tests to determine the correctness of the solution
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print (test())
