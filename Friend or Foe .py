def friend(x):
    
    friends = []
    
    for i in x :
        if len(list(i)) == 4:
            friends.append(i)
    return friends