def one_down(txt):
    if type(txt) != str :
        return "Input is not a string"
    
    txt = list(txt)
    
    y = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y1 = "abcdefghijklmnopqrstuvwxyz"
    y = list(y)
    
    txt1 = []
    
    for i in txt :
        if i in y:
            x = y.index(i) - 1
            txt1.append(y[x])
        elif i in y1:
            x = y1.index(i) - 1
            txt1.append(y1[x])
        elif i not in y or i not in y1:
            txt1.append(i)
            
    return "".join(txt1)