
# coding: utf-8

# In[1]:

import itertools as it

def is_palindrome(n):
    return str(n) == str(n)[::-1]

a = range(900, 1000)
palindromes = [(p[0], p[1], p[0] * p[1]) for p in it.product(a,a) if is_palindrome(p[0] * p[1])]
sorted(palindromes, key = lambda x: x[2])


# In[ ]:



