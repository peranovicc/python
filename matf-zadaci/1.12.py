def pairs(a,b,c,d):
    '''
    Function that generates list of pairs (x,y) such that,
    x is in [a,b] and y is in [c,d]
    '''
    return list([x,y] for x in range(a,b+1) for y in range(c,d+1))


print(pairs(3,5,1,6))

