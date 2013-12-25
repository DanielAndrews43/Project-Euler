def iterPrime(num):
    '''
    iterates through the num to find largest factor
    '''
    x = 3
    answer = 0
    while num-x != 0:
        if float(num)/x == float(num/x):
            num/=x
            answer = num
        else:
            x+=2
    return answer