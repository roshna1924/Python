import numpy as np

b=(np.random.uniform(20, size=20))
c=(b.reshape(4,5))
print(c)
x=(np.max(c,axis=1))
l=x.reshape(-1,1)
print(l)
c = np.where(c==l,0,c)
print("\n Updated matrix is below: \n")
print(c)  # Printing final updated matrix
