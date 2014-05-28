
# coding: utf-8

# In[32]:

import itertools as it
import math

pairs = ((i,j) for i in it.count() for j in range(i + 1))
candidates = (x[0] * x[1] * math.sqrt(x[0]**2 + x[1]**2) for x in pairs if sum(x) + math.sqrt(x[0]**2 + x[1]**2) == 1000)
candidates.next()


# In[ ]:



