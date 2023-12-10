def count_bits(n):
    number = n
    list1 = []

    while int(number) >= 1 :
        if int(number) % 2 == 1 :
            list1.append(1)
        elif int(number) % 2 == 0 :
            list1.append(0)
        number /= 2
    
    l = list1.count(1)
    
    return l   