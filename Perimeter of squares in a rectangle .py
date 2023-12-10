def perimeter(n):
    p = [1, 1]
    
    for i in range(n - 1):
        p.append(p[-2] + p[-1])
    return sum(p)*4