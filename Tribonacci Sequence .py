def tribonacci(signature, n):
    if n != 2 and n != 1 and n!= 0:
        for i in range(n-3) :
            s = signature[-1] + signature[-2] + signature [-3]
            signature.append(s)
    elif n == 2 :
        signature1 = signature.copy()
        signature.clear()
        signature.append(signature1[0])
        signature.append(signature1[1])
        return signature
    elif n == 1 :
        signature1 = signature.copy()
        signature.clear()
        signature.append(signature1[0])
        return signature
    elif n == 0:
        return []
    return signature
