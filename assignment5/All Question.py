import numpy as np
import statistics as st
'''
# Mean and Standard deviation
ar1=np.array([2,5,1,8,5,3,9,7])
print(ar1)
print("Mean of the array is :",ar1.mean())
print("Standard deviation of array is :",st.stdev(ar1))
print()
# to check none of the element is zero
ar2=np.array([1,2,3,4,5,6])
#ar2=np.array([1,2,3,0,6,2])
if(ar2.all()):
    print("Array does not contain zero element")
else:
    print("Array contain zero element")
print()


# creating 3x3x3 matrix
ar3=np.arange(27).reshape(3,3,3)
print(ar3)
print()
'''
'''
#covariance of two matrix
m1=np.array([1,2,3,14,15,16,7,8,9]).reshape(3,3)
m2=np.array([11,12,13,4,5,6,17,18,19]).reshape(3,3)
print(m1)
print(m2)
print(np.cov(m1)) 
'''
m3=[-1,4,9,-4,-2]
print(np.abs(m3))
