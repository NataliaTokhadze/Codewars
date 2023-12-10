def longest(a1, a2):
    a1 = set(list(a1))
    a2 = set(list(a2))
    
    a3 = sorted(a1 | a2)
    a3 = "".join(a3)
    return a3