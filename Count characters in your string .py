def count(s):
    
    if s != " " :
        ss = list(s)

        dict1 = {}
        times = []
    
        z = 0
        for i in ss:
            letter = ss.count(i)
            times.append(letter)
        while z < len(ss):
            dict1.update({ss[z] : times[z]})
            z += 1
        return dict1
    
    else:
        return {}