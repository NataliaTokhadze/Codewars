def small_enough(array, limit):
    yes = []
    no = []
    
    for i in array :
        if i <= limit :
            yes.append(i)
        else:
            no.append(i)
            
    if len(no) == 0 :
        return True
    else:
        return False