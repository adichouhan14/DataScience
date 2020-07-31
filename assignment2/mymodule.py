def oddSum(n):
    s=0
    for i in range(1,n,2):
        s+=i
    return s

def printSquares(n):
    for i in range(1,n+1):
        print(i**2,end=" ")