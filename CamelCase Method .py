def camel_case(s):
     
    ss = s.split(" ")
    
    sss = []
    
    for i in ss:
        y = i.capitalize()
        sss.append(y)
    z = "".join(sss)
    z = str(z)
    
    return z