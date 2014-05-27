
# coding: utf-8

# In[1]:

from collections import deque
import itertools as it

def sieve(q, n):
    for q_i in q:
        if n % q_i == 0:
            return False
        if q_i > n / q_i:
            return True


# In[3]:

#%%time
q = deque([2])
for candidate in it.count(3, 2):
    if sieve(q, candidate):
        q.append(candidate)  

    if q[-1] > 2000000:
        break
        
print sum(list(q)[:-1])


# In[ ]:



