llist=[2,6,3,7,4,8]

# Q1. Smallest value from list
print("Smallest value is :",min(llist))

# Q2. Removing even no

def removingEvenPlaces(l1):
    return [l1[i] for i in range(len(l1)) if i%2!=0]

print(removingEvenPlaces(llist))


# Q3. generating dictionary
def squareDict(n):
    d={}
    for i in range(1,n+1):
        d[i]=i**2
    return d

n=5
print(squareDict(n))

# Q4. remove duplicates

removeDuplicates = lambda llist : list(set(llist))

l1=[1,1,2,2,3,4,4,5,6,6]
print(removeDuplicates(l1))

# Q5. any element same

def anySame(l1,l2):
    l1=set(l1)
    l2=set(l2)
    if len(l1.intersection(l2))==0:
        return False
    return True

llist1=[1,2,3,4,5]
llist2=[0,7,8,9,5]
print(anySame(llist1,llist2))
        
