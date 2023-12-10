def odd_or_even(numbers):
    
    odd = "odd"
    even = "even"
    
    if sum(numbers) % 2 == 0 :
        return even
    elif sum(numbers) % 2 == 1 :
        return odd