
# coding: utf-8

# In[1]:

from collections import deque
import itertools as it

# Using the fundamental theorem of arithmetic
def sieve(q, n):
    for q_i in q:
        if n % q_i == 0:
            return False
        if q_i > n / q_i:
            return True


# In[4]:

#%%timeit
q = deque([2])
for candidate in it.count(3, 2):
    if sieve(q, candidate):
        q.append(candidate)  

    if len(q) == 10001:
        break
        
print q[-1]


# In[ ]:



