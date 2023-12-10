def filter_list(l):
    'return a new list with the strings filtered out'
    
    ll = []
    
    for i in l :
        if type(i) == type(1) :
            ll.append(i)
    
    return(ll)