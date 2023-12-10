def scramble(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s22 = set(s2)
    
    w = []
    
    for i in s22:
        if s1.count(i) >= s2.count (i):
            w.append(1)
    
    if len(w) == len(s22) :
        return True
    else:
         return False