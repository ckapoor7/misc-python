def search(pattern, text):
    """Return true if pattern appears anywhere in text """
    if pattern.startswith('^'):
        return match(pattern[1:] ,text) #Match the remaining pattern
    else:
        return match('.*' + pattern ,text) #Match any character any number of times

def match(pattern, text):
    """Return true if a pattern appears at the start of the text"""
    if pattern == '':
        return True #Always occurs
    elif pattern == '$':
        return (text == '')
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[1:]
        if op == '*':
            return match_star(p, pat, text)
        elif op == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and
                match(pattern[1:], text[1:]))

def match1(p, text):
    """Return true if first character of text matches
    pattern character p """
    if not text: return False
    return p == '.' or p == text[0]

def match_star(p, pattern, text):
    """Return true if any number of char p,
    followed by a pattern matches text """
    return (match (pattern, text) or
            (match1 (p, text) and
             match_star (p, pattern, text[1:])))
