
# coding: utf-8

# In[3]:

def collatz_step(n):
    return n/2 if n % 2 == 0 else 3*n + 1

def collatz_seq_len(_n, memo):
    l = 0
    n = _n
    while n > 1:
        n = collatz_step(n)
        l = l + 1
        if str(n) in memo:
            l = l + memo[str(n)]
            n = 0
    memo[str(_n)] = l

memo=dict()
for i in range(1,1000000, 2):
    collatz_seq_len(i, memo)
max(memo.items(), key=lambda x:x[1])


# In[ ]:



