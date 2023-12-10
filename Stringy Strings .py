def stringy(size):
    
    stringy = []
    
    if size % 2 == 0:
        for i in range(int(size/2)):
            stringy.append("1")
            stringy.append("0")
    elif size % 2 == 1 :
        for i in range(int(size/2)):
            stringy.append("1")
            stringy.append("0")
        stringy.append("1")
    
    stringy = "".join(stringy)
    
    return stringy