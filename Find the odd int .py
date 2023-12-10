def find_it(seq):

    seqq = list(seq)

    seqqq = set(seqq)

    for i in seqqq:
        s = seqq.count(i)
        if s % 2 == 1 :
            return i