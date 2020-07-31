
''' lamda function '''
print()
summ=lambda x,y:(x+y)
print(summ(10,20))






''' Take no and reverse it '''

def reverseNum(n):
    return int(str((str(n)[::-1])))

reverseNumLambda = lambda n : int(str((str(n)[::-1])))

print(reverseNum(245224))
print(reverseNumLambda(123456))
