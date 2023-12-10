def is_valid_walk(walk):
    
    w = []
    
    x = 1 
    y = -1
    c = 2
    v = -2
    
    if len(walk) != 10 :
        return False
    
    if len(walk) == 10 :
        for i in walk :
            
            if i == "n" :
                w.append(x)
                
            elif i == "w":
                w.append(c)
                
            elif i == "s" :
                w.append(y)
                
            elif i == "e":
                w.append(v)
                
        if sum(w) == 0 :
            return True
        else: 
            return False